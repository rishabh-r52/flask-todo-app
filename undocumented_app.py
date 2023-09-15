
from flask import Flask, request, render_template, redirect

from flask_sqlalchemy import SQLAlchemy

from datetime import datetime

app = Flask(__name__) 

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route('/', methods=['GET', 'POST']) 
def hello_world():
    if request.method == "POST":
        print("\npost\n")

        form_title = request.form['title']
        form_desc = request.form['desc']

        if form_title and form_desc:
            todo = Todo(title=form_title, desc=form_desc)
            todo.verified = True
        
            db.session.add(todo)
            db.session.commit()

    allTodo = Todo.query.all()
    return render_template('index.html', allTodo=allTodo)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method == "POST":
        print("\nupdate post\n")

        form_title = request.form['title']
        form_desc = request.form['desc']

        if form_title and form_desc:
            todo = Todo.query.filter_by(sno=sno).first()

            todo.title = form_title
            todo.desc = form_desc
            
            db.session.add(todo)
            db.session.commit()

            return redirect('/')
        
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=1999)