from flask import Flask,Blueprint,session,redirect,url_for,render_template,request
from model import student,question,answer,db

forum=Blueprint("forum",__name__)

@forum.route("/ask",methods=["POST","GET"])
def ask():
    if "id" not in session:
        return redirect(url_for("auth.login"))
    if request.method=="POST":
        title=request.form["title"]
        body=request.form["body"]
        newquestion=question(title=title,body=body,user_id=session["id"])
        db.session.add(newquestion)
        db.session.commit()
        return f"<h1>i will add a html template here for home</h1>"
    else:
        return render_template("forum.html")