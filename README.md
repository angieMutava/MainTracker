# Mantenimiento
This is a web application that allows reporting of maintainance and repair requests, to track the maintenance process and escalate unusual delays.

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
###Upgrading the database.
```
python manage.py db upgrade
```
###Run the server
```
python manage.py runserver
```