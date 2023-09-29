# v1
from flask import Flask, render_template, request
from custom import info_, warning_

info_(text='Запуск файла')
app = Flask(__name__)

# @app.route('/')
@app.route('/', methods=['GET'])
def index() -> render_template:
    """Основная вкладка"""
    return render_template('index.html')

@app.route('/send', methods=['POST', 'GET'])
def send():
    """Получение данных из html"""
    a = request.form['name']
    info_(text=a)
    return render_template('index.html')

info_(text='Файл прогружен')
if __name__ == "__main__":
    "Запуск кода"
    warning_(text='Запуск кода')
    app.run(debug=True, host="localhost", port="3030")