from flask import render_template, request, Flask, redirect
from custom import info_, warning_, error_
import requests
from config import url, headers
from postgresql import datab

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index() -> render_template:
    """Основная вкладка"""
    data = datab().select_all_users()
    return render_template('index.html', users_data=data)
    # return render_template('send.html')

@app.route('/add_message', methods=['GET'])
def hgfg() -> render_template:
    """Основная вкладка"""
    return render_template('add_message.html')

@app.route('/send', methods=['POST', 'GET'])
def send():
    """Получение данных из html"""
    a = request.form['message']
    if a == '':
        return redirect('http://localhost:3040')

    data = {
        'phone': '89515009197',
        'message': a,
        'callback_url': 'http://localhost:3040/'
    }

    response = requests.post(url, headers=headers, json=data)
    response_json = response.json()
    check_responce(response_json=response_json)
    
    return redirect('http://localhost:3040')

@app.route('/number', methods=['POST', 'GET'])
def number():
    num = request.form.get('phone_number')
    print(num)
    # items = []
    # items.append(num)
    # print(items)

def check_responce(response_json) -> None:
    try:
        message_id = response_json['id']
        get_response = requests.get(url=f'{url}/{message_id}', headers=headers)
        get_response_json = get_response.json()
        if get_response_json['status'] == 'Success':
            info_(text=f"{get_response_json['content']}, {get_response_json['phone']}, {get_response_json['id']}")
        elif get_response_json['status'] == 'Failure':
            error_(text=f"{get_response_json['content']}, {get_response_json['phone']}, {get_response_json['id']}")
    except:
        error_code = response_json['status']
        if int(error_code) == 401:
            error_detail = response_json['detail']
        elif int(error_code) == 429:
            error_detail = response_json['detail']
        elif int(error_code) == 500:
            error_detail = response_json['detail']
        error_(text=error_detail)

def upload_route() -> bool:
    warning_('Upload route files')
    return True