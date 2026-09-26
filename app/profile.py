from flask import Blueprint,session,render_template,redirect,url_for,request
from .model import db,student

profile=Blueprint("profile",__name__)

PFP_OPTIONS = [
    "https://api.dicebear.com/7.x/bottts/svg?seed=1",
    "https://api.dicebear.com/7.x/bottts/svg?seed=2",
    "https://api.dicebear.com/7.x/bottts/svg?seed=3",
    "https://api.dicebear.com/7.x/adventurer/svg?seed=Felix",
    "https://api.dicebear.com/7.x/adventurer/svg?seed=Aneka",
    "https://api.dicebear.com/7.x/avataaars/svg?seed=1",
    "https://api.dicebear.com/7.x/avataaars/svg?seed=2",
    "https://api.dicebear.com/7.x/avataaars/svg?seed=3",
    "https://i.redd.it/vvzpigme0ds61.jpg"
]

@profile.route("/user")
def user():
    if "id" in session:
        user=db.session.get(student,session["id"])
        return render_template("user.html",user=user, pfp_options=PFP_OPTIONS)
    else:
        return redirect(url_for("auth.login"))
    
@profile.route("/change_pfp", methods=["POST"])
def change_pfp():
    if "id" in session:
        new_pfp = request.form.get("pfp")
        if new_pfp in PFP_OPTIONS:
            user = db.session.get(student, session["id"])
            user.pfp = new_pfp
            db.session.commit()
        return redirect(url_for("profile.user"))
    return redirect(url_for("auth.login"))
