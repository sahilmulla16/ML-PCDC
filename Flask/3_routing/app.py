from flask import Flask

app = Flask(__name__)

@app.route('/mhssce')
def basic():
    return '<h1>Hello World;</h1>'

@app.route('/mhssce/<name>')
def greets(name):
    return f'Hello {name} Mulla '

if __name__ == '__main__':
    app.run (debug = True)