#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import logging
from logging.handlers import RotatingFileHandler
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from langchain.chains import ConversationChain
from langchain.memory import ConversationSummaryBufferMemory
from langchain_core.messages import SystemMessage
from langchain_core.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
)

# Load environment variables securely
load_dotenv(override=True) 

# Global conversation state
LOG_LEVEL = 'INFO'
MAX_LOG_SIZE = 5 * 1024 * 1024  # 5MB

# Dictionary to store memory for each user
user_memories = {}

###########################################################################################################################
# LLM Model Setup 
repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"
llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    task="text-generation",
    max_new_tokens=4096,
    top_k=8,
    top_p=0.8,
    typical_p=0.8,
    temperature=0.001,
    repetition_penalty=1.20,)

llm_engine_hf = ChatHuggingFace(llm=llm)

###########################################################################################################################
def setup_user_logging(user_id, user_name):
    """Set up a rotating log file for each user."""
    logger = logging.getLogger(f"user_{user_id}")
    
    # Check if the logger already has handlers to avoid adding them multiple times
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s - %(message)s")

        # Create a directory for user logs if it doesn't exist
        if not os.path.exists("user_logs"):
            os.makedirs("user_logs")

        # Create a rotating log handler for the specific user
        file_handler = RotatingFileHandler(f"user_logs/chatlog_{user_id}_{user_name}.log", maxBytes=2*1024*1024, backupCount=5)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger


###########################################################################################################################
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles messages from users."""
    user = update.effective_user
    user_message = update.message.text
    user_id = user.id

    # Setup user-specific logger
    user_logger = setup_user_logging(user_id, user.full_name)
    user_logger.info(f"User: {user_message}")

    try:
        await context.bot.send_chat_action(chat_id=update.effective_chat.id, action="typing")

        # Retrieve or create memory for the user
        if user_id not in user_memories:
            memory = ConversationSummaryBufferMemory(llm=llm_engine_hf, max_token_limit=2048, return_messages=True)
            user_memories[user_id] = memory
        else:
            memory = user_memories[user_id]

        template_messages = [
            SystemMessage(content="<|begin_of_text|><|start_header_id|>system<|end_header_id|> \
                You are a helpful assistant that answers accurately and concrectly only in the same language in which the user is talking<|eot_id|>"),
            MessagesPlaceholder(variable_name="history"),
            HumanMessagePromptTemplate.from_template("{input}"),
        ]
        prompt_template = ChatPromptTemplate.from_messages(template_messages)

        # Create conversation chain with user's memory
        conversation = ConversationChain(llm=llm_engine_hf, memory=memory, prompt= prompt_template)

        # Generate response
        response = conversation.predict(input=user_message)

        # Log and send bot's response
        user_logger.info(f"Bot: {response}")
        await update.message.reply_text(response)

    except Exception as e:
        user_logger.error(f"Error in handle_message: {str(e)}")
        await update.message.reply_text("Sorry, something went wrong. We're working to fix it! ")

###########################################################################################################################
def main():
    bot_token = os.getenv('BOT_TOKEN')
    application = Application.builder().token(bot_token).build()
    # application.bot_data.clear()

    # Message Handler setup
    message_handler = MessageHandler(filters.TEXT, handle_message)
    application.add_handler(message_handler)

    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
