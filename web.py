from bottle import route, run, template
from pack.bib import*

@route('/hello/<name>')
def index(name):
    return template('<b>Olá {{name}}</b>!', name=name)

#http://localhost:8081/hello/unimar
run(host='localhost', port=8081)