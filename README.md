# 🔎 Web Surfing ChatBot 🤖 💬
## 🚀 A streamlit chatbot powered by 🦜🔗 LangChain, SerpAPI, and OpenAI LLM"

---
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://web-surfing-chatbot.streamlit.app/)

An LLM based ChatBot that allows users to ask questions and get real-time answers by searching the web using OpenAI, LangChain, and SERPAPI.

## Overview

This project aims to provide a simple and intuitive interface for users to interact with a ChatBot capable of searching the web in real-time. The ChatBot leverages the power of Large Language Model (LLM), LangChain for natural language understanding and SERPAPI for fetching search results.

## Features

- Real-time web search capabilities powered by OpenAI, LangChain and SERPAPI.
- User-friendly interface built with Streamlit.
- Easy setup and configuration using environment variables for API keys.

## Installation

To run the Web Surfing ChatBot locally, follow these steps:

1. Clone this repository:
```
git clone https://github.com/yourusername/web-surfing-chatbot.git
cd web-surfing-chatbot
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Set up API keys:
- Get an [OpenAI API key](https://platform.openai.com/account/api-keys)
- Get an [SERP API key](https://serpapi.com/)      
- Set the `OPENAI_API_KEY` and `SERPAPI_API_KEY` environment variables or provide it as Input.

4. Run the ChatBot:
```
streamlit run src/main.py
```

## Usage

1. Open the ChatBot interface in your web browser by navigating the local URL provided by Streamlit.
2. Enter the keys if not setup as Env variables.
3. Enter your query in the text input field.
4. Press Enter to submit your query.
5. View the ChatBot's response in real-time.

## Contributing

Contributions to the Web Surfing ChatBot project are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

















