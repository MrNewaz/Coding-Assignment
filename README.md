## Language used: 
* Python v3.10.1

<br/>


## Framework used: 
* Django v4.0.1,
* Django Rest Framework v3.13.1

<br/>

## Database used: 
* SQLite 


<br/>


## Repository Structure:

```
|-- Pipfile
|-- Pipfile.lock
|-- README.md
|-- core
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   `-- wsgi.py
|-- db.sqlite3
|-- manage.py
`-- user
    |-- __init__.py
    |-- admin.py
    |-- apps.py
    |-- migrations
    |   |-- __init__.py
    |-- models.py
    |-- serializers.py
    |-- tests.py
    |-- urls.py
    `-- views.py
```
<br/>


## Installation Instructions:

## Step 1(Download):
* Download [python 3.10.1](https://www.python.org/downloads/)

<br/>

## Step 2(Install):
* Run 'python-3.10.1-amd64.exe' as administrator.
* Don't forget to check add to path(windows)

<br/>

## Step 3(Repository):
* Git Clone 'https://github.com/MrNewaz/Coding-Assignment.git'
* Or Download code from the repository.

<br/>

## Step 4(Virtual Environment):
* Open the folder in an IDE(e.g. VSCode) and Run 'pipenv shell' in the terminal to activate virtual environment.

<br/>

## Step 5(Install Dependencies):
* Run 'pipenv install' in the terminal to install all dependencies.

<br/>



## Step 6(Migrations):
* Run 'python manage.py makemigrations'.
* Run 'python manage.py migrate'. 

<br/>

## Step 7(Adding Superuser):
* Run 'python manage.py createsuperuser' in the terminal and create a superuser to access admin panel by adding username, email(optional) and password.

<br/>

## Step 8(Run App):
* Run 'python manage.py runserver' to start the server.

<br/>

## Step 9(Test App):
* Run 'python manage.py test' for testing APIs.

<br/>

## Done!:
* That's all. Thank you. Have a nice day.


<br/>

# Urls(After Step 8):

## [Admin Pannel](http://127.0.0.1:8000/admin/)
## [Parent Route](http://127.0.0.1:8000/user/parent/)
## [Child Route](http://127.0.0.1:8000/user/child/)

