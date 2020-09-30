# School
Django REST API for a school system

## Features
### Implemented
  - Signup/Login
  - JWT authentication
  - Password update
  - Basic Permissions

### To be implmented
  - Pemissions based on internal Django groups
  - Seperate Forgot password view

### Endpoints
    https://localhost/auth/                # rest_framework auth urls
    https://localhost/auth/login/
    https://localhost/auth/logout/
    https://localhost/api/          
    https://localhost/api/users/           # list users
    https://localhost/api/users/<int:pk>/  # user details

## Setup locally
1. Clone the repo on your machine.
    ```
    git clone https://github.com/ExpressHermes/School.git
    ```
2. In the repo folder, create a virtualenv and activate it.
    ```
    python -m ven env
    source env/bin/activate
    ```
3. Install all dependencies
    ```
    pip install -r requirements.txt
    ```
4. Run makemigrations for `api` app followed by migrate command
    ```
    python manage.py makemigrations api
    python manage.py migrate
    ```
5. Run server
    ```
    python manage.py runserver
    ```
5. Open `https://127.0.0.1:8000/api/`.
