# Step-by-step instruction for how to setup virtual env and start.


# 1. Create virtual environment (if not created)
    -$ python3 -m venv environment-name

# 2. Start virtual environment
    -$ source appenv/bin/activate

# 2.1 How to stop virtual environment
    -$ deactivate appenv

# 3. Install requirements
    -$ pip3 install -r requirements.txt

# 4. Start django app locally, be in the inner app_project folder
    -$ python3 manage.py runserver

# 4.1 Start django on server (if not running) !! HAS TO BE IN VIRTUAL ENVIRONMENT and in the project folder
    -$ python3 manage.py runserver 10.0.0.194:8000