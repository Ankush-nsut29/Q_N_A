from flask import Flask, Blueprint,render_template
from model import student,question,answer

home=Blueprint("home",__name__)

@home.route("/home")
def feed():
    all_questions=question.query.all()
    all_questions=all_questions[::-1]
    return render_template("feed.html",all_questions=all_questions)

