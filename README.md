# Q&A Platform

A simple Q&A platform built with Flask and SQLAlchemy where students can ask and answer questions.

## Project Structure
- `app/`: Contains the main application code (Blueprints, Models, HTML Templates, and Static files).
- `instance/`: Contains the generated SQLite database (`student.db`).
- `run.py`: The entry point for the web application.

## How to Run Locally

1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   - **Windows**: `venv\Scripts\activate`
   - **Mac/Linux**: `source venv/bin/activate`

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python run.py
   ```

The application will be accessible at `http://127.0.0.1:5000/`.
