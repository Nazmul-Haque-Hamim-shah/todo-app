
from flask import Flask,render_template,url_for,request,redirect,session
from db import db,Tasks,User
from werkzeug.security import check_password_hash,generate_password_hash #FOr hasing password
import psw


p=psw.psw()
key=psw.sec()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=p
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()



app.secret_key=key


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/add",methods=["POST","GET"])
def add():
    if request.method=="POST":
        task=request.form.get("task")
        new_task=Tasks(text=task)
        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for("dash"))




@app.route("/update/<int:id>",methods=["POST","GET"])
def update(id):
    task=Tasks.query.get_or_404(id)
    if request.method =="POST":
        task.text=request.form.get("task")
        db.session.commit()
        return redirect(url_for("dash"))

@app.route("/delete/<int:id>")
def delete(id):
    task = Tasks.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("dash"))


@app.route("/sing",methods=["GET","POST"])
def sing():
    if request.method == "POST":
        name=request.form.get("name")
        email=request.form.get("email")
        psw=request.form.get("psw")
        hash_psw=generate_password_hash(psw)

        user=User(
            name=name,
            email=email,
            password=hash_psw
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))

    return render_template("sing.html")



@app.route("/login",methods=["POST","GET"])
def login():
    if request.method == "POST":

        email=request.form.get("email")
        psw=request.form.get("psw")
        user=User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password,psw):
            session["user_id"]=user.id
            session["user_name"]=user.name
            return redirect(url_for("dash"))

        else:
            return "INVALID CREDENTCIAL"

    return render_template("login.html")



@app.route("/dash")
def dash():
    if "user_id" not in session:
        return redirect(url_for("login"))

    tasks = Tasks.query.all()


    return render_template("dash.html",name=session["user_name"],tasks=tasks)
