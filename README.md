# Django ToDo App

This is a basic ToDo web application built with Django.  
It allows users to sign up, log in, and manage their personal tasks.

## Features
- User signup/login/logout
- Create, edit, delete tasks
- Mark tasks as complete/incomplete
- Pagination
- Account Deletion


## Setup Instructions

```bash
# Clone the project
git clone https://github.com/AnmolDevero/todo_project.git
cd todo_project

# Create virtual environment
python -m venv venv
venv\Scripts\activate      # On Windows
source venv/bin/activate # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Apply migrations and run the server
python manage.py migrate
python manage.py runserver
```
