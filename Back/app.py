from flask import Flask
from flask_cors import CORS

api = Flask(__name__)
CORS(app)


@api.route('/')
def hello():
    return 'Hello, World!'

@api.route('/new app')
def hello():
    return 'New App'

if __name__ == '__main__':
    api.run(debug=True)