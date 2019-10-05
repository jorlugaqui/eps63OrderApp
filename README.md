**Orders API**

This is a very small API (one endpoint) written with Flask framework, for academic purposes. 

The `/order` endpoint will enqueue a task in Kafka for processing a custmer's order.

*How to run it*

Local:

`FLASK_APP=app.py flask run`

Go to http://localhost:5000/order

Prod:

`gunicorn --bind 0.0.0.0:8000 wsgi:app`

Go to http://localhost:8000/order


