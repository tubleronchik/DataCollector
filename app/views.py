from flask import Flask, render_template
from app import app, db
from app.models import Data
from flask import request

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/success", methods = ['POST'])
def success():
    if(request.method == 'POST'):
        age_ = request.form['age']
        country_ = request.form['country']
        data = Data(age_,country_)
        db.session.add(data)
        db.session.commit()
        return render_template("success.html")





