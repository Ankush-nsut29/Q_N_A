# Q&A Platform

A clean, simple Q&A platform built with **Flask** and **SQLAlchemy** where students can ask questions, share answers, and collaborate.

## ✨ Features

- **User Authentication:** Secure registration and login system for students.
- **Ask Questions:** Users can post questions to the community.
- **Answer Questions:** Users can help peers by submitting answers to existing questions.
- **Discussion Feed:** A chronological feed displaying all recent questions.
- **Relational Database:** Stores users, questions, and answers using SQLite with SQLAlchemy ORM.

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask, Werkzeug
- **Database:** SQLite3, Flask-SQLAlchemy
- **Frontend:** HTML, CSS (Jinja2 Templates)

## 📂 Project Structure

```bash
├── app/
│   ├── templates/     # HTML templates (Jinja2)
│   ├── static/        # Static files (CSS, JS, Images)
│   ├── model.py       # SQLAlchemy Database Models
│   ├── home.py        # Home/Feed and Answer Routes
│   ├── auth.py        # Authentication Routes (Login/Register)
│   ├── forum.py       # Question posting routes
│   └── __init__.py    # App Initialization
├── instance/
│   └── student.db     # SQLite Database (Auto-generated)
├── requirements.txt   # Python Dependencies
└── run.py             # Application Entry Point
```

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

- Python 3.x installed on your machine.

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd Q_N_A
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   - **Windows:** 
     ```bash
     venv\Scripts\activate
     ```
   - **Mac/Linux:** 
     ```bash
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application:**
   ```bash
   python run.py
   ```
   *Note: The database (`instance/student.db`) will be automatically created when you run the app for the first time.*

6. **Access the web app:**
   Open your browser and navigate to `http://127.0.0.1:5000/`.

## 🤝 Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the issues page.
