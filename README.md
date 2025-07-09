# 🧠 Toyo AI Assistant

Toyo AI is a multifunctional web app powered by Google Gemini and LangChain. It provides two main features:

- 💬 **Toyo Chat** – An AI chatbot that responds to user questions using natural language understanding.
- 🌐 **Toyo Translate** – A multilingual translator that supports 20+ global languages.

Built with **Python** and **Streamlit**, this app is designed for simple local use and free deployment via Streamlit Community Cloud.

---
```

## 📁 Project Structure
├── Toyo_App.py # Main app combining chat & translation
├── Toyo_Chat.py # Standalone chatbot code
├── Toyo_Translate.py # Standalone translator code
├── requirements.txt # List of dependencies
├── .gitignore # Ignore env files, pycache, etc.
└── README.md # Project documentation
```


---

## 🚀 Features

### 💬 Toyo Chat
- Natural language conversation with Gemini Pro
- Maintains full chat history in session
- Clean Streamlit UI with submit button

### 🌐 Toyo Translate
- Translates text between 20+ languages
- User selects input and output languages
- Powered by Gemini via LangChain prompt chaining

---

## 🛠️ Setup Instructions (Local)

1. **Clone the repository**
   ```bash
   git clone https://github.com/kaveeshagimhan/Toyo-Chat.git
   ```
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
3. **Install dependencies**
  - streamlit
  - langchain
  - langchain-google-genai
  - python-dotenv

   ```bash
   pip install -r requirements.txt
   ```
5. **Set your Gemini API Key**
   - Create a .env file:
   ```env
   GOOGLE_API_KEY=your_google_gemini_api_key
   ```
6. **Run the app**
   ```bash
   streamlit run Toyo_App.py
   ```
## 🖼️ Screenshots
### 💬 Chat Mode
![Screenshot 2025-07-09 162418](https://github.com/user-attachments/assets/257b8707-2a84-400e-b02e-bad661986f27)
### 🌐 Translate Mode
![Screenshot 2025-07-09 162456](https://github.com/user-attachments/assets/fb7aa2a7-1456-4767-beeb-2a720dce4701)



  

