Nearby Shops Web App
====================

Overview
--------

The Nearby Shops Web App is a Django-based web application that utilizes GeoDjango to display shops closest to a user's location. This project demonstrates how to build a location-based application using Django, GeoDjango, and PostgreSQL with PostGIS.

Features
--------

-   **Location-Based Search**: Finds and displays shops based on proximity to a given location.
-   **GeoDjango Integration**: Uses GeoDjango for geospatial queries and mapping.
-   **PostgreSQL with PostGIS**: Stores and manages spatial data efficiently.
-   **Admin Interface**: Provides a user-friendly admin panel to manage shops.

Tools & Technologies
--------------------

-   **Python 3**: Programming language.
-   **Django**: Web framework for developing the application.
-   **GeoDjango**: Django module for geographic web applications.
-   **PostgreSQL**: Database for data storage.
-   **PostGIS**: Extension for PostgreSQL to handle spatial data.
-   **Docker**: Containerization tool for setting up PostgreSQL and PostGIS.

Prerequisites
-------------

-   Python 3.x
-   Docker (for PostgreSQL and PostGIS setup)
-   pip (for Python package management)
-   venv (for creating a virtual environment)
-   This project was programmed on the Linux system so that you will not encounter any problems. Use **Linux** or **WSL** for this project

Setup Instructions
------------------

### 1\. Install Dependencies

#### Python 3

Ensure Python 3 is installed. You can download it from [Python's official website](https://www.python.org/).

Verify installation:

```sh 
python3 --version
```

#### GeoDjango Dependencies

Install the required libraries using apt-get or equivalent package manager:

```sh 
sudo apt-get install gdal-bin libgdal-dev
sudo apt-get install python3-gdal
sudo apt-get install binutils libproj-dev
```

### 2\. Set Up PostgreSQL and PostGIS

#### 1\.Use Docker to quickly set up PostgreSQL and PostGIS:

```sh
docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5432:5432 kartoza/postgis:9.6-2.4
```
#### 2\. Or download it localy on system:
- Install PostgreSQL
```bash
sudo apt install postgresql postgresql-contrib
```
This will install PostgreSQL and some additional utilities.
-    Install PostGIS
```bash
sudo apt install postgis postgresql-<version>-postgis-<version>
```
Replace <version> with the version of PostgreSQL you have installed. For example, if you’re using PostgreSQL 14, you would use postgresql-14-postgis-3.
-   Verify Installation
```bash
psql --version
```
#### 3\.Create a New Database and Enable PostGIS
-   Switch to the PostgreSQL User:
```bash
sudo -i -u postgres
```
-   Start the PostgreSQL Interactive Terminal:
```bash
psql
```
-   Create a New Database (replace your_database_name with your desired name):
```sql
CREATE DATABASE your_database_name;
```
-   Connect to the Database:
```sql
\c your_database_name
```
-   Enable PostGIS Extension:
```sql
CREATE EXTENSION postgis;
```
-   You can also enable additional extensions if needed:
```sql
CREATE EXTENSION postgis_topology;
```


### 3\. Create and Activate a Virtual Environment

Create a virtual environment for the project:

```sh 
python3 -m venv env
source env/bin/activate
```

### 4\. Install Project Dependencies

```sh
pip install -r requirements.txt
```

### 7\. Add Initial Data

Create a migration to load initial data from `data.json`.:

```sh
python manage.py migrate
```

### 6\. Run the Development Server

Start the Django development server:

```sh
python manage.py runserver
```

Access the application at `http://localhost:8000/` and the admin interface at `http://localhost:8000/admin/`.

Contributing
------------

If you want to contribute to this project, please fork the repository and submit a pull request. Make sure to follow the coding standards and include tests for new features.

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
----------------

you must change database settings in `nerbyshops/settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'your databas', # change it 
        'USER': 'your username',    # change it 
        'PASSWORD': 'your password',    # change it 
        'HOST': 'localhost',
        'PORT': '5432'
    }
}
```
