# HOME Connect Pro

HOME Connect Pro is an application designed to streamline property management, listing, and inquiry processes. It supports multiple user roles including Clients, Property Purchasers, and Salespersons.

## Features

- User Registration and Login
- User Roles: Client, Property Purchaser, Salesperson
- Profile Management
- Property Listing and Details
- Property Search (geolocation enabled)
- Inquiry System (Create, Track, and Respond to Inquiries)

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)
- Virtualenv (optional but recommended)
- SQLite (if you are using SQLite as your database)

### Clone the Repository

```bash
git clone https://github.com/yourusername/HomeConnectPro.git
cd HomeConnectPro
Create and Activate a Virtual Environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Dependencies:

pip install -r requirements.txt
Configuration
Database Setup

Apply Migrations: 
python manage.py migrate

Create a Superuser:
python manage.py createsuperuser
Running the Development Server

Load data:
python manage.py loaddata db.json

python manage.py runserver
Usage
Access the Application:
Open your web browser and navigate to http://127.0.0.1:8000.

Register and Log In:
Register a new account and log in to access the application's features.

Property Management:
Property Purchasers can list new properties and manage existing listings.

Inquiries:
Clients can create inquiries about properties, and Salespersons can respond to these inquiries.
