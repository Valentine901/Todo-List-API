# A REST API for managing personal todo lists, with JWT authentication.

# Features
    - Registration, and Login user (authentication)
    - Create, fetch, update and delete todo list
    - Only the owner can perform the above action on his    todo list

# Tech Stack
    - Python 3.13.1
    - Django REST Framework
    - Django built-in Sqlite3 database
    - JWT (Json Web Token)

# Project Structure
```
todo/
    ├── app          # Holds todo logic
    ├── user         # Holds user and authentication logic
    ├── todo         # Holds the project logics and settings
    ├── db.sqlite3   #Holds the project database tables(models)
    ├── manage.py    #Django manager for running migrations and others managers commands
    └── README.md
```


## Gettng Started

### Prerequisites
    - Python 3.13 or newer
    - Git 

### Installation 
    1. Create virtual environment by running python -m venv (name of your virtual environment)
    2. Activate your env by running: (on windows: venv\Scripts\activate) , (on mac: source venv/bin/activate)
    3. Install djangorestframework, djangorestframework-simplejwt (django will be included)

Clone the repositoru and enter the project folder:
    ```bash
    git clone <my repo link>
    cd todo

Create a virtual environment:
    ```bash
    python -m venv venv
    ```

Activate it:
    - Windows: `venv\Scripts\activate`
    - macOS / Linux: `source venv/bin/activate

Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

Create the database tables:
    ```bash 
    python manage.py migrate
    ```

Start the server:
    ```
    python manage.py runserver
    ```

The API is now available at `http://127.0.0.1:8000/`
