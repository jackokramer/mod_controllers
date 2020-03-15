from flask import render_template, redirect, request	# we now need fewer imports because we're not doing everything in this file!
# if we need to work with the database, we'll need those imports:    
from config import db
from models import Dojo, Users,

def index():
    dojos = Dojo.query.all()
    return render_template("index.html", dojos= dojos)

def dojo():
    add_dojo = Dojo(
        name  = request.form['name'],
        city = request.form['city'],
        state = request.form['state']
    )
    db.session.add(add_dojo)
    db.session.commit(add_dojo)
    return redirect('/')

def ninja():
    add_ninja = User(
        first_name = request.form['first_name'],
        last_name = request.form['last_name'],
        dojo = request.form['add_doj']
    )
    db.session.add(add_ninja)
    db.session.commit(add_ninja)
    return redirect('/')
