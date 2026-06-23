from flask import Blueprint,session,render_template,redirect,url_for
from model import db,student

profile=Blueprint("profile",__name__)

@profile.route("/user")
def user():
    if "id" in session:
        user=db.session.get(student,session["id"])
        return render_template("user.html",user=user)
    else:
        return redirect(url_for("auth.login"))
    
