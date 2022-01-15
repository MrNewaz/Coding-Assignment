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
.
|-- Pipfile
|-- Pipfile.lock
|-- README.md
|-- core
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- views.py
|   `-- wsgi.py
|-- db.sqlite3
|-- manage.py
|-- templates
|   `-- index.html
`-- user
    |-- __init__.py
    |-- admin.py
    |-- apps.py
    |-- migrations
    |   |-- __init__.py
    |-- models.py
    |-- serializers.py
    |-- tests
    |   |-- __init__.py
    |   |-- test_child_urls.py
    |   |-- test_models.py
    |   `-- test_parent_urls.py
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
* After Python is installed, run, 
```
python -m pip install --upgrade pip
```
* Then run,  
```
pip install pipenv
```


<br/>

## Step 3(Repository):
* Clone the repository,
```
git clone https://github.com/MrNewaz/Coding-Assignment.git
```
* Or download code from the [repository](https://github.com/MrNewaz/Coding-Assignment.git).

<br/>

## Step 4(Virtual Environment):
* Open the folder in an IDE(e.g. VSCode) and run this in the terminal to activate virtual environment,
```
pipenv shell
``` 


<br/>

## Step 5(Install Dependencies):
* Run this in the terminal to install all dependencies,
```
pipenv install
```

<br/>



## Step 6(Migrations):
* Run this creating new migrations based on the changes in your models,
```
python manage.py makemigrations
```
* Then Run this to apply the migrations to the database,
```
python manage.py migrate
```

<br/>

## Step 7(Superuser):
* Run this in the terminal and create a superuser to access admin panel by adding username, email(optional) and password, You will need username and password to login to the admin panel,
```
python manage.py createsuperuser
```

<br/>

## Step 8(Run App):
* Run this to start the app,
```
python manage.py runserver
```

<br/>

## Step 9(Test App):
* Run this for testing API routes and models.
```
python manage.py test
```

<br/>

## Done!:
* That's all. Thank you. Have a nice day.


<br/>

## Urls(After Step 8):

## [Admin Pannel](http://127.0.0.1:8000/admin/)
## [Parent Route](http://127.0.0.1:8000/user/parent/)
## [Child Route](http://127.0.0.1:8000/user/child/)

