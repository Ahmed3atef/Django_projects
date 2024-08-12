# Django Puppy Store API

This project is a CRUD-based RESTful API for a Puppy Store using Django and Django REST Framework.

## Objectives

By the end of this tutorial, you will be able to:

- Discuss the benefits of using Django REST Framework for bootstrapping the development of a RESTful API
- Validate model querysets using serializers
- Appreciate Django REST Framework's Browsable API feature for a cleaner and well-documented version of your APIs
- Practice test-driven development

## Project Structure

```
puppy_store/
├── manage.py
├── puppies/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations/
│   │   └── __init__.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_models.py
│   │   └── test_views.py
│   ├── urls.py
│   └── views.py
├── puppy_store/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── readme.md
└── requirements.txt
```

## RESTful Structure

| Endpoint      | HTTP Method | CRUD Method | Result                  |
|---------------|-------------|-------------|-------------------------|
| `puppies`     | GET         | READ        | Get all puppies         |
| `puppies/:id` | GET         | READ        | Get a single puppy      |
| `puppies`     | POST        | CREATE      | Add a single puppy      |
| `puppies/:id` | PUT         | UPDATE      | Update a single puppy   |
| `puppies/:id` | DELETE      | DELETE      | Delete a single puppy   |

## Setup

### Database Setup

This project uses PostgreSQL. Create a database named `puppy_store_drf`:

```bash
$ psql
# CREATE DATABASE puppy_store_drf;
CREATE DATABASE
# \q
```

Install psycopg2 to interact with the Postgres server via Python:

```bash
(env)$ pip install psycopg2==2.7.1
```

### Database Configuration

Update the `DATABASES` configuration in `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'puppy_store_drf',
        'USER': '<your-user>',
        'PASSWORD': '<your-password>',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
```

## Model

The `Puppy` model is defined in `puppies/models.py`:

```python
from django.db import models

class Puppy(models.Model):
    """
    Puppy Model
    Defines the attributes of a puppy
    """
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    breed = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_breed(self):
        return self.name + ' belongs to ' + self.breed + ' breed.'

    def __repr__(self):
        return self.name + ' is added.'
```

## Installation

1. Clone the repository
2. Create a virtual environment and activate it
3. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
4. Run migrations:
   ```
   python manage.py migrate
   ```
5. Start the development server:
   ```
   python manage.py runserver
   ```

## Running Tests

To run the tests, use the following command:

```
python manage.py test
```

## API Documentation

For detailed API documentation, run the server and navigate to the browsable API interface provided by Django REST Framework.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
