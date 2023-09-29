from flask import render_template, request, Flask, redirect
from custom import info_, warning_
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index() -> render_template:
    """Основная вкладка"""
    return render_template('index.html')

@app.route('/send', methods=['POST', 'GET'])
def send():
    """Получение данных из html"""
    a = request.form['name']
    info_(text=a)
    return redirect('http://localhost:3030')

def upload_route() -> bool:
    warning_('Upload route files')
    return True