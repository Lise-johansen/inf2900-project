[![Django CI](https://github.com/uit-inf-2900/Team11/actions/workflows/django.yml/badge.svg)](https://github.com/uit-inf-2900/Team11/actions/workflows/django.yml)[![VUE App CI](https://github.com/uit-inf-2900/Team11/actions/workflows/node.js.yml/badge.svg)](https://github.com/uit-inf-2900/Team11/actions/workflows/node.js.yml)
# Step-by-step instruction for how to setup virtual env and start.


# 1. Create virtual environment (if not created)
    -$ python3 -m venv environment-name

# 2. Start virtual environment
    -$ source environment-name/bin/activate

# 2.1 How to stop virtual environment
    -$ deactivate environment-name

# 3. Install requirements
    -$ pip3 install -r requirements.txt

# 4. Start django app locally, be in the inner app_project folder
    -$ python3 manage.py runserver

# 4.1 Start django on server (if not running) !! HAS TO BE IN VIRTUAL ENVIRONMENT and in the project folder
    -$ python3 manage.py runserver 10.0.0.194:8000

# 5. Download vue-cli
    -$ npm install -g @vue/cli
    -$ npm install crypto-js
    -$ npm install axios

# 5.1 Start vue server (MUST be done inside vue-app folder) also use a different window for this as you need to run both simultaniously
    -$ npm run serve

# 5.2 Build app for development
    -$ npm run build
