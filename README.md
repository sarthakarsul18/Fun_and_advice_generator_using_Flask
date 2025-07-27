# 🎉 Fun Generator App

A simple and fun mini-project that combines **Flask (backend)** and **Streamlit (frontend)** to deliver random jokes and life advice using free public APIs.

---

## 🚀 Features

- Get a **random joke** with a punchline
- Get **life advice** instantly
- Clean and interactive **Streamlit UI**
- Backend powered by **Flask API**
- Uses 100% **free APIs** (no API key needed)

---

## 🔧 Requirements

Install the required libraries:

```bash
pip install flask streamlit requests
```

▶️ How to Run

1️⃣ Start the Flask Backend\
```bash
python app.py
```
This will start your API server at http://localhost:5000

2️⃣ Start the Streamlit Frontend\
Open a new terminal and run:

```bash 
streamlit run frontend.py
```
The UI will open in your browser automatically at http://localhost:8501

🔍 Available Endpoints (Flask API)\
Route	Description\
/joke	Returns a random joke\
/advice	Returns a random advice

🙌 Author\
Made with ❤️ by Sarthak
