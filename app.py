from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Todo(db.Model):
    sno =  db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    decs = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow , nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

@app.route("/", methods=['GET', 'POST'])
def show_todo():
    """
    Renders the index.html template and handles the creation of new todo items.

    Returns:
        rendered template: index.html with all_todo data
    """
    if request.method == 'POST':
        title = request.form['title']
        decs = request.form['desc']  
        todo = Todo(title=title, decs=decs)
        db.session.add(todo)
        db.session.commit()
    all_todo = Todo.query.all()
    return render_template('index.html', all_todo=all_todo)

@app.route("/update/<int:sno>", methods=['GET', 'POST'])
def update_todo(sno):
    """
    Renders the update.html template and handles the updating of a specific todo item.

    Args:
        sno (int): The serial number of the todo item to be updated.

    Returns:
        rendered template: update.html with todo data
        redirect: to the home page after updating the todo item
    """
    if request.method == 'POST':
        title = request.form['title']
        decs = request.form['desc']  
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.decs = decs
        db.session.add(todo)
        db.session.commit()
        return redirect("/")
    
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route("/delete/<int:sno>")
def delete_todo(sno):
    """
    Deletes a specific todo item.

    Args:
        sno (int): The serial number of the todo item to be deleted.

    Returns:
        redirect: to the home page after deleting the todo item
    """
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()

    return redirect("/")

@app.route("/about")
def about():
    """
    Renders the about.html template.

    Returns:
        rendered template: about.html
    """
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True, port=8000)
