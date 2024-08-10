# Notable Django API

A simple RESTful API for a note-taking application built with Django and django-tastypie.

## Project Overview

This project implements a basic API for managing notes, similar to Google Keep. It provides CRUD (Create, Read, Update, Delete) operations for notes using Django and django-tastypie.

## Features

- RESTful API endpoints for notes
- CRUD operations on notes
- Simple Note model with title, body, and creation timestamp
- Basic authorization for API access (suitable for development only)

## Technologies Used

- Python
- Django
- django-tastypie

## Project Structure

```
notable_django/
├── api/
│   ├── models.py
│   └── resources.py
├── notable_django/
│   ├── settings.py
│   └── urls.py
└── manage.py
```

## Setup and Installation

1. Ensure you have Python installed on your system.
2. Install required packages:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Start the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- List all notes: GET `/api/note/`
- Retrieve a specific note: GET `/api/note/<id>/`
- Create a new note: POST `/api/note/`
- Update a note: PUT `/api/note/<id>/`
- Delete a note: DELETE `/api/note/<id>/`

## Usage

You can use tools like Postman or curl to interact with the API. Here's an example of creating a new note using curl:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"title":"New Note", "body":"This is a new note"}' http://localhost:8000/api/note/
```

## Security Note

The current authorization setup is suitable for development only. For production use, implement proper authentication and authorization mechanisms.


