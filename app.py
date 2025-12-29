
from flask import Flask,render_template,url_for,request,redirect
from db import db,Tasks,User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DB_PASS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    tasks=Tasks.query.all()
    return render_template("index.html",tasks=tasks)


@app.route("/add",methods=["POST","GET"])
def add():
    if request.method=="POST":
        task=request.form.get("task")
        new_task=Tasks(text=task)
        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for("index"))




@app.route("/update/<int:id>",methods=["POST","GET"])
def update(id):
    task=Tasks.query.get_or_404(id)
    if request.method =="POST":
        task.text=request.form.get("task")
        db.session.commit()
        return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    task = Tasks.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))




