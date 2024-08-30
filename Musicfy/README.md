# Musicfy

![coverage](https://img.shields.io/badge/coverage-80%25-yellowgreen)
![version](https://img.shields.io/badge/version-1.2.3-blue)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

A Django-REST backend project with semple frontend , Musicfy is website for hosting musics and play it , the front-end made by ChatGPT
and i programmed the backend , it using postgres database to store the info for each music that uploaded .

!['website frontend'](/image.png)
!['website backend'](/swagger.png)

**Table of Contents**

- [Installation](#installation)
- [Execution / Usage](#execution--usage)
- [Technologies](#technologies)


## Installation

edit this code :
```python 
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'musicfy', # database name
        'USER':'postgres', # your username for postgres
        'PASSWORD':'postgres', # your password
        'HOST':'localhost',
        'PORT':5432,
    }
}
```

On macOS and Linux:

```sh
$ python3 -m venv env
$ source ./env/bin/activate
$ pip3 install -r requirements.txt
```

On Windows:

```sh
PS> python -m venv env
PS> .env\Script\activate
PS> pip install -r requirements.txt
```

## Execution / Usage

To run muscify, fire up a terminal window and run the following command:

```sh
$ python manage.py migrate
$ python manage.py runserver
```



## Technologies

Musicfy uses the following technologies and tools:

- [Python](https://www.python.org/): ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- [PostgresSQL](https://www.postgresql.org): ![PostgresSQL](https://img.shields.io/badge/postgres-%252307405e.svg?style=for-the-badge&logo=postgresql&logoColor=blue)
- [Django](https://www.djangoproject.com): ![Django](https://img.shields.io/badge/Django-3670A0.svg?style=for-the-badge&logo=django&logoColor=green)