from route import upload_route, app
from custom import info_

if __name__ == "__main__":
    "Starting code"
    if upload_route():
        info_(text='Files "route" upload')
    app.run(debug=True, host="localhost", port="3040")