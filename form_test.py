from flask import Flask
from flask import render_template
from flask import request

@app = Flask(__name__)

def shutdown():
    func = request.environ.get('werkzeug.server.shutdown')
    if func in None:
            raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown')
def shutdown(): #콜백함수
    shutdown_server()
    return 'Server shuttin down..'

@app.route('/mainpage', methods=['POST'])
def mainpage(): #콜백함수
    name = request.form['name']
    nameData = {'name' : name}
    return render_template('test5.html', **nameData)

@app.route('/')
def root():
    return render_template('test4.htm')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8888, debut = True)
