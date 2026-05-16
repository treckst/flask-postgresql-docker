from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! Flash is running'

@app.route('/about')
def about():
    return 'This is a simple Flask application.'

@app.route('/contact')
def contact():
    return 'Contact us at abc'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)