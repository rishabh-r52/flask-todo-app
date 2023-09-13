# Import Flask module from flask package
from flask import Flask 

# Used to render template files onto flask route
from flask import render_template 

# Create an app using name as '__name__'
app = Flask(__name__) 

# Refers to the url 127.0.0.1:1999/
@app.route('/') 
def hello_world():
    # Returns content of index.html
    return render_template('index.html')
    # return 'Hello, World!'

# Refers to the url 127.0.0.1:1999/home/
@app.route('/home')
def home_print():
    return "<h1>This is home route</h1>"

# If the name of the app is '__main__',
# It will run the app at port=1999
if __name__ == '__main__':
    app.run(debug=True, port=1999)