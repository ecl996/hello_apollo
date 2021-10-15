from bottle import route, run, template
import datetime

@route('/hello')
def index():
    return f'<b>Hello {datetime.datetime.now()}</b>!'

run(host='0.0.0.0', port=8080)
