# Django CRM 

This project has been created for educational purposes and serves as a hands-on experience for learning Django, a popular Python web framework. It's designed to help you understand the fundamentals of web development, user authentication, and database management with Django.

## About the Project

This project aims to create a simple CRM (Customer Relationship Management) system. It includes features for user registration, login, adding, updating, and deleting customer records. The project demonstrates how to use Django's built-in authentication system and how to interact with a MySQL database.

## Features

- User registration and authentication.
- Adding, updating, and deleting customer records.
- Database management with MySQL.
- Basic HTML templates and form handling.

## Getting Started

To run this project locally on your machine, follow these steps:

- git clone https://github.com/torbalansky/django-crm.git (Clone this repository to your local machine.)
- cd django-crm (Navigate to the project directory.)
- python -m venv venv (Create a virtual environment. Optional but recommended).
- Activate the virtual environment.
**On Windows**
venv\Scripts\activate

**On macOS and Linux**
source venv/bin/activate

- pip install -r requirements.txt (Install project dependencies.)
- python manage.py migrate (Apply database migrations.)
- python manage.py runserver (Start the development server.)