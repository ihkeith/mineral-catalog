# Hank's Humongous Minerals

A humorous django application dedicated to our favorite detective, Hank Schrader.

## Application Overview

Team Treehouse Python Techdegree Project 6: A Mineral Catalog App in Django. This application is designed to store data on minerals in a sqlite database and server that information dynamically on the site page. Users can select a mineral to view the details.

## Dependencies

See `requirements.txt` for more details.

- Python 3.6
- Django 2.2.2

## Usage

- clone the repo to your computer
- You'll need to run the migration to create the database and populate the data.
  - from the commandline, run:
    ```bash
    python3 manage.py makemigrations minerals
    python3 manage.py migrate minerals
    ```
- from the root of that folder, run `python3 manage.py runserver`
- In your browser, open `localhost` to see the site