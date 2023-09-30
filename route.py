from flask import render_template, request, Flask, redirect
from custom import info_, warning_, error_
import requests
from config import url, headers
from postgresql import datab
from time import sleep
from multiprocessing import Process
 

import json

app = Flask(__name__)


list_message = [
    'm1',
    'm2',
    'm3',
    'm4',
    'm5',
    'm6',
    'm7',
    'm8',
    'm9',
    'm10',
    'm11',
]


list_number = []

@app.route('/', methods=['GET', 'POST'])
def index() -> render_template:
    """Главная страница"""
    data = datab().select_all_users()
    return render_template('index.html', users_data=data)


@app.route('/phone-number', methods=['POST'])
def handle_phone_number() -> str:
    phone_number = request.json['phone_number']

    if phone_number in list_number:
        list_number.remove(phone_number)
        error_(phone_number)
    else:
        list_number.append(phone_number)
        info_(phone_number)
    return 'ok'



@app.route('/send_all', methods=['POST', 'GET'])
def send_all():
    a = request.form['message']
    if a == '':
        return redirect('http://localhost:3040')
    
    process = Process(target=send_message_all, args=(a,list_number,))
    process.start()

    return redirect('http://localhost:3040')





@app.route('/send_all_users', methods=['POST', 'GET'])
def send_all_users():
    process = Process(target=send_message_all_user, args=(list_message,list_number,))
    process.start()

    return redirect('http://localhost:3040')




def send_message_all(a, list_number) -> None:
    for i in list_number:
        data = {
            'phone': i,
            'message': a,
            'callback_url': 'http://localhost:3040/'
        }
        response = requests.post(url, headers=headers, json=data)
        response_json = response.json()
        check_responce(response_json=response_json)
        sleep(0.15)

def send_message_all_user(list_message, list_number):
    for i in list_number:
        for u in list_message:
            data = {
                'phone': i,
                'message': u,
                'callback_url': 'http://localhost:3040/'
            }
            response = requests.post(url, headers=headers, json=data)
            response_json = response.json()
            check_responce(response_json=response_json)
            sleep(0.15)

    # return render_template('send.html')

@app.route('/add_message', methods=['GET'])
def add_message() -> render_template:
    """Отправка сообщений"""
    return render_template('add_message.html')

@app.route('/history', methods=['GET'])
def history() -> render_template:
    """История"""
    return render_template('history.html')


@app.route('/send', methods=['POST', 'GET'])
def send() -> redirect:
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



# @app.route('/number', methods=['POST', 'GET'])
# def number():
#     num = request.form.get('phone_number')
#     print(num)
#     # items = []
#     # items.append(num)
#     # print(items)

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






@app.route('/next', methods=['GET'])
def next_main() -> redirect:
    print(list_number)
    
    return redirect('http://localhost:3040')





def upload_route() -> bool:
    """Функция прогрузки"""
    return True