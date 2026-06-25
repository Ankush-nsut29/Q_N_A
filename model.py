from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class student(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(50),nullable=False)
    email=db.Column(db.String(50),nullable=False,unique=True)
    password=db.Column(db.String(50),nullable=False)

class question(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(100),nullable=False)
    body=db.Column(db.Text)
    user_id=db.Column(db.Integer,db.ForeignKey("student.id"))

class answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text)
    question_id = db.Column(db.Integer, db.ForeignKey("question.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("student.id"))

db.relationship("answer",backref="question")
