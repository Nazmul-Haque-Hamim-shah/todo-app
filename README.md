# 📝 Todo App with Flask, SQLAlchemy & Authentication

A simple yet scalable **Todo web application** built using **Flask**, **SQLAlchemy**, and **PostgreSQL/SQLite**, featuring full **CRUD functionality**, **user authentication**, and **session-based login system**.
This project is designed as a foundation for building a larger (“mega”) application step by step.

---

## 🚀 Features

- ✅ User Sign Up & Login  
- 🔐 Secure Password Hashing  
- 🧠 Session-based Authentication  
- 📝 Todo Task CRUD (Create, Read, Update, Delete)  
- 👤 User-specific access (logged-in users only)  
- 🗄️ Database integration using SQLAlchemy  
- 🎨 Responsive UI with Bootstrap  
- 🌍 Ready for deployment (Railway / PostgreSQL)

---

## 🛠️ Tech Stack

- **Backend:** Flask (Python)
- **Database ORM:** Flask-SQLAlchemy
- **Database:** SQLite (development) / PostgreSQL (production)
- **Authentication:** Werkzeug (password hashing)
- **Frontend:** HTML, Bootstrap 5
- **Session Management:** Flask Sessions

---

## 📁 Project Structure
|
|
todo_app/
│
├── app.py              # Main Flask application
├── db.py               # Database initialization & models
├── requirements.txt    # Project dependencies
│
├── templates/
│   ├── index.html      # Todo list page
│   ├── login.html      # Login page
│   ├── sing.html       # Sign up page
│
└── static/
    └── (optional css/js)

---

## 🔐 Authentication Flow

1. User signs up with name, email, and password.
2. Passwords are hashed using Werkzeug.
3. User logs in using valid credentials.
4. Session stores logged-in user information.
5. Protected routes require active session.
6. Logout clears session data.

---

## 📝 Todo CRUD System

- Create new tasks
- View all tasks
- Update existing tasks
- Delete tasks permanently

---

## ⚙️ Setup & Installation

1. Create virtual environment  
2. Install dependencies  
3. Run Flask server  

---

## 🔮 Future Improvements

- Per-user todo filtering
- Flask-Login integration
- REST API version
- Better security & validation

---

## 👨‍💻 Author

Hamim Shah  
Built for learning Flask & backend development 🚀
