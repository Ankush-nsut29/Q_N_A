from flask import request,render_template,redirect,url_for,Blueprint,session
from model  import student,db
auth=Blueprint("auth",__name__)

@auth.route("/register",methods=["POST","GET"])
def register():
    if request.method=="POST":
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        s=student(name=name,email=email,password=password)
        db.session.add(s)
        db.session.commit()
        return redirect(url_for("auth.login"))
    else:
        return render_template("auth/register.html")    
    
@auth.route("/login",methods=["POST","GET"])
def login():
    if request.method=="POST":
        email=request.form["email"]
        password=request.form["password"]
        student_found=student.query.filter_by(email=email).first()
        if student_found and student_found.password==password:
            session["id"]=student_found.id
            return redirect(url_for("profile.user"))    
        else:
            return redirect(url_for("auth.login"))
    else:
        return render_template("auth/login.html")    

@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))