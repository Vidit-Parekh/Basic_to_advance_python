from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'This is home page.'

@app.route('/index')
def index():
    return 'This is index page.'

if __name__ == '__main__':
    app.run(debug=True)


