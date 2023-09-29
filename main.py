from flask import Flask, render_template
from custom import info_, warning_

info_(text='Запуск файла')
app = Flask(__name__)

@app.route('/')
def index() -> render_template:
    """Основная вкладка"""
    return render_template('index.html')

@app.route('/about')
def about() -> str: 
    "О нас"
    return render_template('about.html')

info_(text='Файл прогружен')
if __name__ == "__main__":
    "Запуск кода"
    warning_(text='Запуск кода')
    app.run(debug=True, host='172.20.10.5')