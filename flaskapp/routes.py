from flask import render_template, url_for, flash, redirect, request, Flask
from flaskapp import app, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required
from flaskapp.forms import RegistrationForm, LoginForm
from flaskapp.models import User


import pandas as pd
import numpy as np
from scipy.spatial.distance import cdist


# messages = [{'title': 'Message One',
#              'content': 'Message One Content'},
#             {'title': 'Message Two',
#              'content': 'Message Two Content'}
#             ]


@app.route("/index", methods=['get', 'post'])
@login_required
def index():
    if request.method == "post":
        category = request.form['category']
        address = request.form['address']
        price = request.form['price']

        latitude = request.json['latitude']
        longitude = request.json['longitude']

        
    return render_template('index.html', 
        cat=[{'cat': 'Attractions'}, {'cat': 'Restaurants'}, {'cat': 'Hotels'}],
        prc=[{'prc': '100-500'}, {'prc': '500-1000'}, {'prc': '1000-3000'}, {'prc': '3000-more'}],
    )
    
@app.route("/category")
def category():
    return render_template('category.html')

@app.route("/listing")
def listing():
    return render_template('listing.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/", methods=['get', 'post'])
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
