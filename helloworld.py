from bottle import route, run, template
import datetime

@route('/hello')
def index():
    message = "<b>Hello " + datetime.datetime.now() + "</b>!"
    return message

run(host='0.0.0.0', port=8080)
