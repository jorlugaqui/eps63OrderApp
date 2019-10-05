from flask import Flask

app = Flask(__name__)

@app.route('/order')
def order():
    return 'Your order'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')