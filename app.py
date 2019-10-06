import os
import boto3
import json
import logging
import watchtower

from flask import Flask, request, abort

app = Flask(__name__)

sns = boto3.client(
    'sns',
    region_name='us-east-2',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')  
)

logs_session = boto3.Session(
    region_name='us-east-2',
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')  
)

logging.basicConfig(level=logging.INFO)
app = Flask("loggable")
handler = watchtower.CloudWatchLogHandler(boto3_session=logs_session)
app.logger.addHandler(handler)
logging.getLogger("werkzeug").addHandler(handler)


@app.route('/order', methods = ['POST'])
def order():
    try:
        order_payload = json.loads(request.data)
    except Exception as e:
        app.logger.error(f'Unable to parse payload {request.data}')
        app.logger.error(e)
        abort(400) 

    try:
        sns.publish(
            TopicArn='arn:aws:sns:us-east-2:624102251302:eps63_orders',    
            Message=json.dumps(order_payload),    
        )
        return 'Your Order is being processed', 200
    except Exception as e:
        app.logger.error(e)
        abort(500, 'Unable to find the specified topic')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')