# FastAPI Google AI Edu Tools 🎓🤖

A FastAPI-based backend integrating Google AI Studio's Gemini APIs to power AI-driven educational tools and services. This project is designed to be the backend foundation for EdTech platforms that require dynamic content generation, Q&A bots, and interactive AI-based features.

---

## 🚀 Features

- ✨ AI-powered Q&A endpoint using Google AI Studio (Gemini 1.5 Flash)
- 👤 User creation and management
- ⚙️ Modular and clean project structure
- 📡 RESTful API with FastAPI
- 🧠 Easily extensible to other AI models
- 💾 SQLite with SQLAlchemy ORM (easy to switch DB)
- ☁️ Ready for cloud deployment (Heroku, GCP, AWS)
- 🔒 Secure API key management with environment variables

---

## 📁 Project Structure

```
fastapi-ai-edu-tools/
├── app/
│   ├── main.py                    # FastAPI app setup
│   ├── models.py                  # SQLAlchemy models
│   ├── schemas.py                 # Pydantic schemas
│   ├── database.py                # DB engine and session
│   ├── google_ai_integration.py   # Google AI Studio integration
│   └── routes/
│       ├── user.py                # /users/ route
│       └── ai.py                  # /ask-ai/ route
├── .env                           # Environment variables (create from .env.example)
├── .env.example                   # Environment variables template
├── requirements.txt
├── setup.sh                       # Quick setup script
└── README.md
```

---

## 🔧 Setup Instructions

### Quick Setup (Recommended)
```bash
# Clone the repository
git clone https://github.com/your-username/fastapi-ai-edu-tools.git
cd fastapi-ai-edu-tools

# Run the setup script
./setup.sh

# Edit .env file with your Google AI Studio API key
nano .env  # or use your preferred editor
```

### Manual Setup

### 1. Clone the repository
```bash
git clone https://github.com/your-username/fastapi-ai-edu-tools.git
cd fastapi-ai-edu-tools
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Add your Google AI Studio API Key
Create a `.env` file in the root directory (or copy from `.env.example`) and add:

```ini
GOOGLE_API_KEY=your_google_ai_studio_api_key_here
```

To get your Google AI Studio API key:
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Click on "Get API key" 
4. Create a new API key or use an existing one
5. Copy the API key and paste it in your `.env` file

### 5. Run the FastAPI server
```bash
uvicorn app.main:app --reload
```
Server will start at: http://127.0.0.1:8000

---

## 🧪 API Endpoints

### ✅ Ask AI
**POST** `/ask-ai/`

Body:
```json
{
    "prompt": "What is Newton's First Law?"
}
```

Response:
```json
{
    "response": "Newton's First Law states that..."
}
```

### ✅ Create User
**POST** `/users/`

Body:
```json
{
    "name": "Ashish",
    "email": "ashish@example.com"
}
```

---

## 📚 Technologies Used

- **FastAPI** — high-performance API framework
- **Google AI Studio** — Gemini AI model integration
- **SQLAlchemy** — ORM for database models
- **Pydantic** — Data validation
- **Uvicorn** — ASGI server
- **python-dotenv** — for environment variable handling

---

## 🚀 Future Enhancements

- 🔐 JWT Authentication
- 🧠 Multiple AI model support (OpenAI, Anthropic, etc.)
- 🧩 Vector DB support (e.g., Pinecone, Chroma)
- 🌐 WebSocket/streaming responses
- 📊 Analytics dashboard
- 🎯 Fine-tuned models for educational content

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👋 Contact

**Built by Aashish Timalsina**
- 📧 aashish@example.com
- 🌐 Danson Solutions

---

Let me know if you'd like:
- Swagger UI screenshots  
- A hosted version (on Render/Heroku)  
- CI/CD setup via GitHub Actions  
- README badges (build passing, license, OpenAI-powered, etc.)  

Happy coding!
