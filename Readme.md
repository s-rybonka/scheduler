# Scheduler

#### Main dependencies: ####
1. Python 3.7
2. Django 2.2
3. Django Rest Framework 3.9
### Quick Start ###
1. git clone git@github.com:s-rybonka/scheduler.git
2. cd to /your_project_folder
3. cp env.example scheduler/.env
4. Create virtualenv: python3 -m venv venv
5. Activate it: source venv/bin/activate
6. Install project dependencies: pip install -r requirements.txt
7. Configure your interpreter in IDE (optional)
8. Apply migrations: ./manage.py migrate
9. Run application: ./manage.py runserver 127.0.0.1:8000

**Note**: Please, exclude optional settings from .env file, if you are not going to override them.
