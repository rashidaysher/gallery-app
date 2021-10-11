### Kiliga_photofraphy Gallery App
This a moringa independent project done at core module using the django framework.

### Contibutors

- Aisha Rashid Ahmed

### Description

<img src = "picha/static/images/Screenshot from 2021-10-11 19-45-13.png" >
Kiliga_photography is a photo gallery web application to showcase images taken from different locations. A user can view photos, see photos based on the location, by clicking on the listed locations in the menu. They can also copy the link to a photo to paste at their discretion. They can also search for photos based on the categories.All photos are podted by the admin.

### Features
* The home page allows users to see various images
* User can see all images per location they were taken
* Users can also search for images based categories
* Admin can upload images from a django dashboard


### Technology used
- python 3.8
- Django framework
- css, bootstrap, html, js
- postgresssql
- Heroku
- Cloudinary

### Live Site
The live site can be found at: https://github.com/rashidaysher/gallery-app


### Prerequisite

* Clone the Repo
* Activate virtual enviroment

### Install dependancies
Install dependancies that will create an environment for the app to run pipenv install -r requirements.txt

### Create Database
* psql
* CREATE DATABASE gallery;

### .env file

Create .env file and paste paste the following filling where appropriate:

SECRET_KEY = '<Secret_key>'
DBNAME = 'gallery'
USER = '<Username>'
PASSWORD = '<password>'
DEBUG = True

### Initial migration
 run initial migrations at:

python3.8 manage.py makemigrations gallery
python3.8 manage.py migrate

### Run the app

python3.8 manage.py runserver
Open terminal on localhost:8000

### Known bugs
None at the moment

### Contact Info

rashidaisha.ara@gmail.com

