# Mantenimiento
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
##Usage
Beginner in python and flask respectively? Ha! Lets walk together.
<br/>
Learning flask as a beginner in web is not easy, especially when you have very many tutorials and have no idea where to start. I have ideally narrowed down to miguel's book and tutorials online.<br/>
######check them here
```
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
```
```
https://flaskbook.com
```
In the links provided you will be guided on how to stucture your application. From the structure you will need to do some configuration to flask for all the dependent softwares you have installed. For instance the config.py file does that for us. The entry point to the application is the python file manage.py that runs the flask application.<br/>

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
###Screenshots
######home page
![alt](https://github.com/angieMutava/MainTracker/blob/master/screenshots/home.PNG "home")