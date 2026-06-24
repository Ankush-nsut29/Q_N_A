from flask import Flask,session,redirect,url_for
from auth import auth
from model import student,db
from profile import profile

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///student.db"
db.init_app(app)    
app.register_blueprint(auth)
app.register_blueprint(profile)
app.secret_key="hbhbs"

@app.route("/")
def index():
    if "id" in session:
        return redirect(url_for("profile.user"))
    return redirect(url_for("auth.login"))

if __name__=="__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)