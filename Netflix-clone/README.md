# Netflix Clone

![coverage](https://img.shields.io/badge/coverage-80%25-yellowgreen)
![version](https://img.shields.io/badge/version-1.2.3-blue)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)

a strem website which clone the Netflix site , programmed with django and used postgres SQL to add data into database.
user can login or signup to browse movies that add to website , website support adding movies from admin site but first you must have supper user account

![front page](/readme_media/readme.png)

**Table of Contents**

- [Installation](#installation)
- [Execution / Usage](#execution--usage)
- [Technologies](#technologies)

## Installation

On macOS and Linux:

```sh
$ python3 -m venv env
$ source .env/bin/activate
$ pip3 install -r requirements.txt
```

On Windows:

```sh
PS> python -m venv env
PS> .env\Script\activate
PS> pip install -r requirements.txt
```

## Execution / Usage

To run Netflix Clone, fire up a terminal window and run the following command:

```sh
$ python3 manage.py migrate
$ python3 manage.py runserver
```

## Technologies

Netflix Clone uses the following technologies and tools:

- [Python](https://www.python.org/): ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
- [PostgresSQL](https://www.postgresql.org): ![PostgresSQL](https://img.shields.io/badge/postgres-%252307405e.svg?style=for-the-badge&logo=postgresql&logoColor=blue)
- [Django](https://www.djangoproject.com): ![Django](https://img.shields.io/badge/Django-3670A0.svg?style=for-the-badge&logo=django&logoColor=green)
