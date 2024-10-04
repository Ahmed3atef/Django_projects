# Online Compiler

A web-based code compilation and execution platform built with Django.

## 🚀 Features

- Supporting python programming languages
- Real-time code compilation and execution
- Syntax highlighting

## 🛠️ Tech Stack

- **Backend**: Django
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

## ⚙️ Installation

1. Create and activate virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Apply database migrations
```bash
python manage.py migrate
```

4. Create a superuser (admin)
```bash
python manage.py createsuperuser
```

5. Start the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser to access the application.

## 📁 Project Structure

```
COMPILER/
├── __pycache__/
├── __init__.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py

home/
├── migrations/
├── __init__.py
├── admin.py
├── apps.py
├── models.py
├── tests.py
├── urls.py
└── views.py

templates/
└── index.html

manage.py
db.sqlite3
```

## 🔧 Configuration

Key settings can be found in `COMPILER/settings.py`:
- Database configuration
- Allowed hosts
- Installed apps
- Middleware
- Templates

## 🔒 Security Considerations

- Ensure DEBUG is set to False in production
- Use environment variables for sensitive data
- Regularly update dependencies
- Implement proper input sanitization for code execution


## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.



