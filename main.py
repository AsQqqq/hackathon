from route import upload_route, app
from custom import info_


if __name__ == "__main__":
    """Запуск кода"""
    if upload_route():
        info_(text='Файл "route" прогрузился')
    # Запуск flask
    app.run(debug=True, host="localhost", port="3040")