# JorJitsu
Full stack database with Python Flask PostgreSQL

To run this fictional Jiu Jitsu school database you must first install the requirements in the requirements.txt 
in a virtual enviorenment like "venv".



open docker container to pgAdmin PostgreSQL database and create a database titled "JorJitsu"

then from main folder in the terminal run these commands 

source venv/Scripts/activate

set FLASK_APP=run.py
export FLASK_ENV=development
flask run
NOTE: app will not work if you havent install all correct packages.

after "flask run" you can acess the front end from your web browser here "http://127.0.0.1:5000/"

I will be adding more tables and columns as I go along but for now we can only add students to the database.
