# caloriecount

Welcome to My Macronutrient Tracker App! This Django-based application, enhanced with ChartJS and Bootstrap. It is designed to help you track your daily food intake and monitor your macronutrient levels.

## Features

- Log your daily food consumption
- Visualize macronutrient intake using ChartJS
- User authentication and personalized profiles
- Responsive design for a seamless user experience

## Technologies Used

- Django
- ChartJS
- Bootstrap
- Database (SQLite3)

## Getting Started

### Prerequisites

Before you can run this app on your local machine, you will need to have the following installed:

- Python 3.9 or higher
- Django 4.2 
- SQLite or the database of your choice

### Installation

Before cloning the repository, it is recommended that you create a virtual environment in which you will run the app. To create a virtual environment, you need to run the command:

python -m venv venv

1. Clone the repository:
   
   git clone https://github.com/torcuata22/caloriecount.git

3. Navigate to the root directory:

   cd myapp

4. Activate your virtual environment:

source venv/bin/activate (if you are using Linux or Macos)
venv\Scripts\activate (if you are a  Windows user)
   
6. Install dependencies by running:

  pip install -r requirements.txt

4. Setup the database:

  python manage.py migrate


##Usage
To run the app, you need to run the following command in the terminal:

python manage.py runserver

Open your browser and navigate to http://localhost:8000.

Sign up for an account or log in if you already have one.

Begin tracking your daily food intake and visualize macronutrient consumption using the provided charts.

This project is licensed under the MIT License.
