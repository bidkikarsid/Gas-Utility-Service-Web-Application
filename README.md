# Gas-Utility-Service-Web-Application


This project is a **Django-based web application** designed to manage customer service requests for a gas utility company. The application allows customers to submit service requests online, track the status of their requests, and view their account information. It also provides an interface for customer support representatives to manage requests and provide support.

## Features

- Customer Portal: 
  - Customers can submit service requests such as installation, maintenance, or billing inquiries.
  - Customers can upload files (e.g., images of problems or documents).
  - Customers can track the status of their service requests in real-time.

- Admin Panel: 
  - Provides an interface for administrators to manage customer accounts and service requests.
  - Admin link is available on the home page for quick access.

- Support Representative Interface: 
  - Support staff can view and manage service requests assigned to them.
  
- Responsive Design: 
  - The web application is mobile-friendly, using Bootstrap for modern and clean design.

## Built With

- Python 
- Django 
- Bootstrap 
- SQLite (default Django database)

## Steps 

2. Create and Activate a Virtual Environment
Using virtualenv (Recommended)
```bash

# Install virtualenv if not installed
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment (Windows)
source venv/Scripts/activate

# Activate the virtual environment (macOS/Linux)
source venv/bin/activate
```
3. Install Dependencies
Once the virtual environment is activated, install the required dependencies:

```bash

pip install -r requirements.txt
Note: Ensure that Django and other dependencies are listed in the requirements.txt file. You can create this file using the command:
```

4. Set Up the Database
Migrate the database to create necessary tables:

```bash

python manage.py makemigrations
python manage.py migrate
```
5. Create a Superuser
To access the Django admin panel, create a superuser:

```bash
python manage.py createsuperuser
Follow the prompts to set up the superuser account.
```
6. Run the Development Server
Start the Django development server:

```bash
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to access the application.
```
7. Access the Admin Panel
To access the admin interface, go to:

```bash

http://127.0.0.1:8000/admin/
Use the superuser credentials you created earlier to log in.
```
## Project Structure
```php
gas_utility/
│
├── customer_service/         # Main app directory
│   ├── templates/            # HTML templates
│   │   └── home.html         # Homepage template
│   ├── static/               # Static files (CSS, JS, images)
│   ├── migrations/           # Database migrations
│   ├── views.py              # View functions
│   ├── models.py             # Data models
│   ├── forms.py              # Form classes
│   ├── admin.py              # Admin configuration
│   └── urls.py               # URL patterns for the app
│
├── gas_utility/              # Project directory
│   ├── settings.py           # Project settings
│   ├── urls.py               # Project-level URL patterns
│   ├── wsgi.py               # WSGI entry point for deployment
│   ├── asgi.py               # ASGI entry point for async support
├── manage.py                 # Django management commands
├── venv/                     # Virtual environment directory (if using virtualenv)
└── README.md                 # Project documentation
```

### Contributing
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request.




