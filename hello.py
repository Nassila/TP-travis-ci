"""A dummy docstring."""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    """A dummy docstring."""
    return "Hello world"

@app.route('/hello/<name>')
def hello(name=None):
    """A dummy docstring."""
    return 'Hello ' + str(name)

if __name__ == "__main__":
    app.run()
