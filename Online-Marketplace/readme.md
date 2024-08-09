# Puddle - A Simple Django Online Marketplace

## Project Overview

Puddle is an educational project designed to teach the basics of Django by building a simple online marketplace. Users can buy and sell items through this platform.

## Features

- User Authentication
- User-to-User Communication
- Personal Dashboard for Managing Items
- Form Handling and Customizations

## Learning Objectives

By working on this project, you will learn:

1. How to set up a Django project
2. Implementing user authentication in Django
3. Creating models for items and user profiles
4. Handling form submissions and data validation
5. Implementing user-to-user messaging
6. Creating a dashboard for users to manage their items
7. Customizing Django forms
8. Basic front-end integration with Django templates

## Getting Started

To get started with Puddle, follow these steps:


1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Apply database migrations:
   ```
   python manage.py migrate
   ```

3. Run the development server:
   ```
   python manage.py runserver
   ```

4. Open your web browser and navigate to `http://localhost:8000` to view the application.

## Project Structure

The project is organized into several Django apps and key files:

- `conversation/`: Handles user-to-user messaging functionality.
- `core/`: Contains core functionality and base templates.
- `dashboard/`: Manages the user's personal dashboard.
- `item/`: Handles item listings, creation, and management.
- `media/`: Stores user-uploaded media files.
- `puddle/`: The main Django project directory.
- `env/`: Virtual environment (not shown in the image, but typically present).
- `db.sqlite3`: SQLite database file.
- `manage.py`: Django's command-line utility for administrative tasks.
- `README.md`: This file, containing project documentation.
- `requirements.txt`: List of Python dependencies for the project.

Each app (conversation, core, dashboard, item) contains its own models, views, and templates specific to its functionality.


## License

MIT License

Copyright (c) [year] [fullname]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


