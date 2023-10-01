from flask import render_template, request, Flask, redirect, abort
from custom import info_, warning_, error_
import requests
from config import url, headers
from postgresql import datab
from time import sleep
from multiprocessing import Process
 
import json

app = Flask(__name__)



list_number = []

@app.route('/', methods=['GET'])
def index() -> render_template:
    """Страница входа в аккаунт админа"""
    return render_template('index.html')


@app.route('/join-to-server', methods=['GET', 'POST'])
def join_to_server() -> render_template:
    """Выбор пользователей"""
    try:
        login = request.form['login']
        password = request.form['password']
        if login == "" or password == "":
            return render_template('index.html')
        else:
            lg = datab().logout(login=login, password=password)
            if not lg:
                return render_template('index.html')
            else:
                data = datab().select_all_users()
                return render_template('select_user.html', users_data=data)
    except:
        return abort(404)

@app.route('/phone-number', methods=['POST'])
def handle_phone_number() -> str:
    """Получение номера телефона из html"""
    phone_number = request.json['phone_number']

    if phone_number in list_number:
        list_number.remove(phone_number)
        error_(phone_number)
    else:
        list_number.append(phone_number)
        info_(phone_number)
    return 'ok'



@app.route('/send_message', methods=['GET', 'POST'])
def add_message() -> render_template:
    """Страница отправки сообщения"""
    if not list_number:
        data = datab().select_all_users()
        return render_template('select_user.html', users_data=data)
    return render_template('message_user.html')



@app.route('/send_all_users', methods=['POST', 'GET'])
def send_all_users():
    message = request.form['message']
    warning_(text=message)
    process = Process(target=send_message_all_user, args=(message,list_number,))
    process.start()

    return redirect('http://localhost:3040/send_message')


def send_message_all_user(message, list_number):
    for i in list_number:
        print(i)
        data = {
            'phone': i,
            'message': message,
            'callback_url': 'http://localhost:3040/'
        }
        # response = requests.post(url, headers=headers, json=data)
        # response_json = response.json()
        # check_responce(response_json=response_json)
        sleep(0.15)



@app.route('/history', methods=['GET'])
def history() -> render_template:
    """История"""
    return render_template('history.html')



def check_responce(response_json) -> None:
    """Просмотр на ошибки запроса"""
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