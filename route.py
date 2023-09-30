from flask import render_template, request, Flask, redirect
from custom import info_, warning_
import requests
from config import url, headers


app = Flask(__name__)



@app.route('/', methods=['GET'])
def index() -> render_template:
    """Основная вкладка"""
    return render_template('index.html')

@app.route('/send', methods=['POST', 'GET'])
def send():
    """Получение данных из html"""
    a = request.form['message']

    data = {
        'phone': '89515009197',
        'message': a,
        'callback_url': 'http://localhost:3030/'
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    message_id = response_json['id']

    get_response = requests.get(url=f'{url}/{message_id}', headers=headers)
    warning_(get_response.text)

    return redirect('http://localhost:3030')

def upload_route() -> bool:
    warning_('Upload route files')
    return True