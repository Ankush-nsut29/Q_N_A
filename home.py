from flask import Flask, Blueprint,render_template,session,redirect,url_for,request
from model import student,question,answer
from model import db,answer,question,student

home=Blueprint("home",__name__)

@home.route("/home")
def feed():
    all_questions=question.query.all()
    all_questions=all_questions[::-1]
    return render_template("feed.html",all_questions=all_questions)

@home.route("/answer/<question_id>", methods=["GET", "POST"])
def answer_page(question_id):
    if "id" not in session:
        return redirect(url_for("auth.login"))
    
    q=db.session.get(question,question_id)

    if request.method == "POST":
        body = request.form["body"]
        new_answer = answer(body=body, question_id=question_id, user_id=session["id"])
        db.session.add(new_answer)
        db.session.commit()
        return redirect(url_for("home.answer_page", question_id=question_id))

    return render_template("answer.html", question=q)