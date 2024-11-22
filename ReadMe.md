# NULLNET AI MODEL

To kick off :

**cd to right directory**
cd aiModel

**Install the requirements**
pip install -r requirements.txt

**cd to root django folder**

**Start the GRPC Server**
python manage.py grpcrunserver

**Start the http Server**
python manage.py runserver

**Use Correct Route**
In browser, route to http://127.0.0.1:8000/api/grpc-trigger/