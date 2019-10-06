**Orders API**

This is a very small API (one endpoint) written with Flask framework, for academic purposes. 

The `/order` endpoint will enqueue a task in Kafka for processing a custmer's order.

*How to run it*

Local:

`AWS_ACCESS_KEY=<your_aws_access_key> AWS_SECRET_ACCESS_KEY=<your_aws_secret_key> FLASK_APP=app.py flask run`

Go to http://localhost:5000/order

Prod:

`AWS_ACCESS_KEY=<your_aws_access_key> AWS_SECRET_ACCESS_KEY=<your_aws_secret_key> gunicorn --bind 0.0.0.0:8000 wsgi:app`

Go to http://localhost:8000/order

Docker:

`docker build -t <your-namespace>/order_app  .`

`docker run -p 8000:8000 -e AWS_ACCESS_KEY=<your_aws_access_key> -e AWS_SECRET_ACCESS_KEY=<your_aws_secret_key> --rm <your-namespace>/order_app`

Go to http://localhost:8000/order

