from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello world"

@app.route('/hello/<name>')
def hello(name=None):
  return 'Hello ' + str(name)

if __name__ == "__main__":
    app.run()