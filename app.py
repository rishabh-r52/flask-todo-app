# -------------------------------------------
# from flask import Flask

# app = Flask(__name__)

# @app.route("/")

# def hello_world():
#     return "<p>Hello World!</p>"

# app.run(debug=True)

# -------------------------------------------

# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

# -------------------------------------------

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/home')
def home_print():
    return "<h1>This is home route</h1>"

if __name__ == '__main__':
    app.run(debug=True, port=1999)