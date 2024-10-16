# 🚀 Conversational AI Bot – Powered by Meta-Llama-3

Welcome to the **Conversational AI Bot**, an intelligent chatbot built using the **Meta-Llama-3-8B** model. This bot is designed for real-time conversations on Telegram, providing smart, context-aware responses that get more refined over time by remembering user interactions.

## 💬 Interacting with the Bot

Try chatting with the bot on Telegram:

👉 [https://t.me/conversational_LB_bot](https://t.me/conversational_LB_bot)

Test its ability to maintain the flow of conversation and see how it adapts to various inputs!

## 🌟 Key Features

- **AI-Driven Conversations**: Powered by **Meta-Llama-3**, the bot generates meaningful, human-like responses, ensuring dynamic interactions.
  
- **Contextual Memory**: With personalized memory for each user, the bot retains conversation context over time, enhancing the quality of its replies.

- **Real-Time Interaction via Telegram**: Fully integrated with the Telegram API, allowing you to chat with the bot instantly.

- **User-Specific Logging**: Creates secure, rotating log files for each user, making it easy to track or review conversations.

- **Environment-Secure**: Sensitive data like API tokens are stored securely using environment variables.

## ⚙️ Requirements

To set up the bot, you’ll need:

- **Python 3.8+**
- **Telegram Bot Token** (Get one from [BotFather](https://core.telegram.org/bots#botfather))
- **Hugging Face API Access** (For using Meta-Llama-3)

## 🚀 Quick Start

### Step 1: Clone the Repository

Start by cloning the repository:

```bash
git clone https://github.com/burna680/Conversational-Chatbot.git
cd Conversational-Chatbot
```

### Step 2: Set Up the Environment

Create a virtual environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Step 3: Configure the Environment

Add your Telegram bot token and you HuggingFace API key to the `.env` file:

```bash
HF_TOKEN= <Your-HuggingFace-API-Key>
BOT_TOKEN=<Your-Telegram-Bot-Token>
```

### Step 4: Run the Bot

Run the bot on Telegram:

```bash
python bot.py
```

Now you can chat with **your** bot on Telegram! 🎉🤖

## 📂 Project Structure

Here's the project layout:

```plaintext
.
├── bot.py                 # Main bot script
├── requirements.txt       # Dependencies
├── .env                   # Environment variables
├── user_logs/             # Logs for each user
└── README.md              # Project documentation
```

## 🤝 Contributing

Want to contribute? Here’s how:

1. **Fork the repo**.
2. **Create a new branch**: `git checkout -b <feature-branch>`.
3. **Commit your changes**: `git commit -am 'Add new feature'`.
4. **Submit a Pull Request**.

All contributions are welcome! 🚀

## 🔮 Future Improvements

Interested in contributing to this project? We welcome all suggestions and ideas! You can explore and work on the features listed in the [TODO](TODO.md) file. Whether you're enhancing existing functionalities or adding new ones, your contributions are always appreciated!

## 📄 License

This project is under the **MIT License**. Check the [LICENSE](LICENSE) file for more information.

## 📚 Resources

Here are some useful links:

- [Meta-Llama-3 Documentation](https://www.llama.com/docs/model-cards-and-prompt-formats/meta-llama-3/)
- [LangChain API Reference](https://python.langchain.com/api_reference/langchain/index.html)
- [Hugging Face Endpoints](https://huggingface.co/docs/hub/endpoints)

## 👨‍💻 About the Developer

Hi! I’m **Lucas**, a passionate Machine Learning Engineer specialized in **NLP** and **Computer Vision**. With over three years of experience, I’ve led various AI-driven projects, including chatbot development and advanced AI systems. 

## 📞 Contact

Feel free to reach out if you have any questions or want to connect!

- [**LinkedIn**](https://www.linkedin.com/in/lucas-burna/en)
- [**Personal Website**](https://burna680.github.io/portfolio/)

