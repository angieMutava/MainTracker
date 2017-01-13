# Mantenimiento
[![Build Status](https://travis-ci.org/angieMutava/MainTracker.png?branch=master)](https://travis-ci.org/angieMutava/MainTracker})
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/dwyl/esta/issues)
<br/>
This is a web application that allows reporting of maintainance and repair requests, to track the maintenance process and escalate unusual delays.

  |Mantenimiento is a spanish word that means maintainance.

##Basic functionalities.
```
1. User Registration
2. User signIn
3. User request maintainance/repair
4. Admin accept/reject a maintainance/repair. In case of a reject provide comment.
5. Admin assign maintainance/repair to relevant user
6. User get a notification once a repair/maintanance has been resolved
7. As admin, I should be able to add names and contacts (phone number) for the people doing maintenance.
``` 
##Guide
Beginner in python and flask respectively? Ha! Lets walk together.Learning flask as a beginner in web is not easy, especially when you have very many tutorials and have no idea where to start. I have ideally narrowed down to miguel's book and tutorials online.<br/>
######check them here
```
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
```
```
https://flaskbook.com
```
In the links provided you will be guided on how to stucture your application. From the structure you will need to do some configuration to flask for all the dependent softwares you have installed. For instance the config.py file does that for us. The entry point to the application is the python file manage.py that runs the flask application.<br/>
##Installation
To get the application up and running on your environment. Follow the procedure.<br/>

1.git clone the repository.
```
https://github.com/angieMutava/MainTracker
```
2.Configure the virtual environment or download a virtual wrapper and configure to an appropriate location in your machine<br/>
3.In your virtual aenvironment run the command.
```
pip -r requirements.txt
```
4.Navigate to the folder MainTracker.<br/>
5.Initialize the database by running the commands illustrated in the later description.<br/>
6.Finally run the application with the command.
```
python manage.py runserver
```

You can download sqlite browser in order to be able to view the tables in the model class inside the model.py.
Open databases and navigate to the root folder and open tracker.sqlite
<br/>
##Requirements
######language
python 2.7 or python 3.0 should be installed in your machine.
######Dependencies
To install the required dependencies for the application to run on your machine run the below command in the virtual environment.
```
pip install -r requirements.txt on your machine.
```
###Initialize the db with the command.
```
python manage.py db init

```
###Migrations
```
python manage.py db migrate
```
###Upgrading the database.
```
python manage.py db upgrade
```
###Run the server
```
python manage.py runserver
```
###Screenshots for the key pages
######home page
![alt](https://github.com/angieMutava/MainTracker/blob/master/screenshots/home.PNG "home")
######index page
![alt](https://github.com/angieMutava/MainTracker/blob/master/screenshots/index.PNG "index")
######admin page
![alt](https://github.com/angieMutava/MainTracker/blob/master/screenshots/admin.PNG "admin")