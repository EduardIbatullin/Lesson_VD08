from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)


def get_random_quote():
    params = {
        "method": "getQuote",
        "format": "json",
        "lang": "ru"
    }
    response = requests.get("https://api.forismatic.com/api/1.0/", params=params)
    if response.status_code == 200:
        data = response.json()
        return data.get('quoteText', 'Цитата не найдена')
    return 'Ошибка при получении цитаты'


@app.route('/')
def index():
    quote = get_random_quote()
    return render_template('index.html', quote=quote)


@app.route('/api/quote')
def quote_api():
    quote = get_random_quote()
    return jsonify({'quote': quote})


if __name__ == '__main__':
    app.run(debug=True)
