from flask import Flask
from flask_cors import CORS
from datetime import ( datetime, date, timedelta )
import requests

api = Flask(__name__)
CORS(api)


@api.route('/')
def hello():
    return 'Hello, World!'

@api.route('/new_app')
def tsla(request):
    if request.method == "GET":
        current_date = date.today()
        current_date_string = current_date.strftime("%Y-%m-%d")
        url = f"https://api.polygon.io/v2/aggs/ticker/TSLA/range/1/day/{current_date_string}/{current_date_string}?adjusted=true&sort=asc&limit=49999&apiKey=nyd1QVoAqt4QVkHYYMqe_5kvFfN40G8D"
        response = requests.get(url)
        data = response.json()

    return f"Received{data['ticker']},{data['v']},{data['c']} "

if __name__ == '__main__':
    api.run(debug=True)