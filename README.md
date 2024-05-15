[![Django CI](https://github.com/uit-inf-2900/Team11/actions/workflows/django.yml/badge.svg)](https://github.com/uit-inf-2900/Team11/actions/workflows/django.yml) [![VUE App CI](https://github.com/uit-inf-2900/Team11/actions/workflows/node.js.yml/badge.svg)](https://github.com/uit-inf-2900/Team11/actions/workflows/node.js.yml)

# Rentopia: Own less, Explore more

## File structure
The repo contains folders for Django backend and Vue Frontend.
The files necessary for the project are these:
    
### Django Structure
- app_project/   
    - airfinn/  
        - templates/    
        - \_\_init\_\_.py   
        - admin.py  
        - apps.py   
        - models.py     
        - test.py   
        - utils.py      
        - views.py  
    - app_project/
        - .env  
        - \_\_init\_\_.py
        - asgi.py
        - authenticat.py
        - settings.py
        - settings_test.py
        - urls.py
        - wsgi.py
    - manage.py
    
### Vue.js Structure
- vue_app/
    - dist/
        - `generated with npm run build`
    - node_modules/
        - `all node packages`
    - public/
        - `public files from npm run build`
    - src/
        - assets/
            - `static images`
        - components/
            - `all vue components`
        - App.vue
        - main.js
        - router.js
    - babel.config.js
    - jsconfig.json
    - package.json    `all packages used for our project`
    - package-lock.json
    - vue.config.js

## Requirements
Start a virtual environment with `python -m venv "environment name"`    
Install requirements.txt in root folder `pip install -r requirements.txt`    

Then install the requirements for Vue.js    
Inside the vue-app folder run `npm install`    
## Compiling
When all the requirements are installed, you can run and host the website.    
First build the Vue front-end with `npm run build`    
Then host the wsgi/asgi file `app_project/app_project/wsgi.py | app_project/app_project/asgi.py` with your chosen host.

## Development hosting
Alternative to compiling the project it can be hosted for development.    
Django: `python manage.py runserver`    
Vue: `npm run serve`
