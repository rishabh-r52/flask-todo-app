# Import Flask module from flask package
from flask import Flask 

# Used to render template files onto flask route
from flask import render_template 

# Used to create a database in python through flask
from flask_sqlalchemy import SQLAlchemy

# Used for datetime
from datetime import datetime

# Create an app using name as '__name__'
app = Flask(__name__) 

# Create a database
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# When attempting to create todo.db, use flask shell (After Flask 3.0+):
# flask shell
# from app import db
# db.create_all()

# But that approach will cause context error in future when creating database
# Use the below approach for creating database
with app.app_context():
    db.create_all()


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# Refers to the url 127.0.0.1:1999/
@app.route('/') 
def hello_world():
    todo = Todo(title="First Todo", desc="Make AI and teach it humanity")
    todo.verified = True
    db.session.add(todo)
    db.session.commit()
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