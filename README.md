# FastAPI AI Edu Tools 🎓🤖

A FastAPI-based backend integrating OpenAI's GPT APIs to power AI-driven educational tools and services. This project is designed to be the backend foundation for EdTech platforms that require dynamic content generation, Q&A bots, and interactive AI-based features.

---

## 🚀 Features

- ✨ AI-powered Q&A endpoint using OpenAI (GPT-3.5/4)
- 👤 User creation and management
- ⚙️ Modular and clean project structure
- 📡 RESTful API with FastAPI
- 🧠 Easily extensible to LangChain, Hugging Face, etc.
- 💾 SQLite with SQLAlchemy ORM (easy to switch DB)
- ☁️ Ready for cloud deployment (Heroku, GCP, AWS)

---

## 📁 Project Structure

```
fastapi-ai-edu-tools/
├── app/
│   ├── main.py                 # FastAPI app setup
│   ├── models.py              # SQLAlchemy models
│   ├── schemas.py             # Pydantic schemas
│   ├── database.py            # DB engine and session
│   ├── openai_integration.py  # GPT call logic
│   └── routes/
│       ├── user.py            # /users/ route
│       └── ai.py              # /ask-ai/ route
├── .env                       # Environment variables
├── requirements.txt
└── README.md
```

---

## 🔧 Setup Instructions

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

### 4. Add your OpenAI API Key
Create a `.env` file in the root directory and add:

```ini
OPENAI_API_KEY=your_openai_key_here
```

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
- **OpenAI API** — GPT-3.5/4 integration
- **SQLAlchemy** — ORM for database models
- **Pydantic** — Data validation
- **Uvicorn** — ASGI server
- **dotenv** — for environment variable handling

---

## 🚀 Future Enhancements

- 🔐 JWT Authentication
- 🧠 LangChain or Hugging Face integration
- 🧩 Vector DB support (e.g., Pinecone, Chroma)
- 🌐 WebSocket/streaming responses
- 📊 Analytics dashboard

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
