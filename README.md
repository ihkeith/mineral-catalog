# Hank's Humongous Minerals

A humorous django application dedicated to our favorite detective, Hank Schrader.

## Application Overview

Team Treehouse Python Techdegree Project 6: A Mineral Catalog App in Django. This application is designed to store data on minerals in a sqlite database and server that information dynamically on the site page. Users can select a mineral to view the details.

## Dependencies

See `requirements.txt` for more details.

- Python 3.6
- Django 2.2.2

## Usage

### Clone the repo to your computer

`git clone https://github.com/ihkeith/mineral-catalog.git`

### Create your virtual environment

From the root of the cloned folder, run:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run migrations

You'll need to run the migration to create the database and populate the data.

From the commandline, run:

```bash
python3 manage.py makemigrations minerals
python3 manage.py migrate minerals
```

### Run the Server

From the root of that folder, run `python3 manage.py runserver`

In your browser, open `localhost` to see the site