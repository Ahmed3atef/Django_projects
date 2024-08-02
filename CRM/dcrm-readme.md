# DCRM (Django Customer Relationship Management)

## Project Overview

DCRM is a Customer Relationship Management system built with Django. It allows users to manage customer records, including creation, reading, updating, and deletion of customer information.

## Project Details

- Project Name: DCRM
- App Name: website
- Python Version: 3.10.2

## Features

- User authentication (login, logout, register)
- View all customer records
- Add new customer records
- View individual customer details
- Update customer records
- Delete customer records

## Project Structure

The project consists of the following main components:

1. `models.py`: Defines the data model for customer records
2. `views.py`: Contains the logic for handling HTTP requests and rendering responses
3. `urls.py`: Defines the URL patterns for the application
4. `db.py`: Initializes the MySQL database (not provided in the code snippet)

### Models

The project uses a single model called `Record` to store customer information:

```python
class Record(models.Model):
    createed_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
```

### Views

The application includes the following views:

1. `home`: Displays all records and handles user authentication
2. `logout_user`: Logs out the current user
3. `register_user`: Handles user registration
4. `customer_record`: Displays details of a specific customer record
5. `delete_record`: Deletes a specific customer record
6. `add_record`: Adds a new customer record
7. `update_record`: Updates an existing customer record

### URLs

The `urls.py` file defines the following URL patterns:

```python
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:pk>/', views.customer_record, name='record'),
    path('add_record/', views.add_record, name='add'),
    path('update_record/<int:pk>/', views.update_record, name='update'),
    path('delete_record/<int:pk>/', views.delete_record, name='delete'),
]
```

## User Interface

The DCRM application has a simple and intuitive user interface. Here's an overview of the main pages:

1. Home Page (Logged In):
   - Displays a table with all customer records
   - Shows columns for ID, Name, Email, Address, City, State, Zipcode, and Created At
   - Provides options to logout and add a new record

   ![Home Page](/CRM/redme-images/home.png)
   *Image 1: Home page showing the list of customer records with options to logout and add a new record.*

2. Customer Record Details:
   - Shows detailed information about a specific customer
   - Includes options to go back, delete the record, or update the record

   ![Customer Record Details](/CRM/redme-images/details.png)
   *Image 2: Detailed view of a customer record with options to update or delete the record.*

3. Login Page:
   - Allows users to log in with their username and password
   - Displays a message when logged out

   ![Login Page](/CRM/redme-images/login.png)
   *Image 3: Login page with fields for username and password, and a message indicating successful logout.*

4. Registration Page:
   - Allows new users to create an account
   - Includes fields for username, first name, last name, email, password, and password confirmation
   - Provides password requirements

   ![Registration Page](/CRM/redme-images/register.png)
   *Image 4: Registration page with fields for creating a new user account and password requirements.*

## Setup and Installation

install all dependencies 
```bash
pip install -r requirements.txt
```
you should change db.py (host, user, passwd) then use it:
```bash
python db.py
```

in `DCRM/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'crm_django',
        'USER':'your mysql username',
        'PASSWORD':'your password',
        'HOST':'localhost',
        'PORT': 3306,
    }
}
``` 

## Usage

```
python manage.py runserver
```

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
