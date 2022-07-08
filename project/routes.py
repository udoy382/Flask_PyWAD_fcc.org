from datetime import date
from project import app
from flask import render_template, redirect, url_for
from project.models import Item, User
from project.forms import RegisterForm
from project import db

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/market')
def market():

    # items = [
    #     {'id': 1, 'name': 'Udoy', 'barcod':1133, 'price':500},
    #     {'id': 2, 'name': 'Mariyam', 'barcod':1453, 'price':900},
    #     {'id': 3, 'name': 'Fariha', 'barcod':1673, 'price':1500}
    # ]

    items = Item.query.all()

    return render_template('market.html', items=items)

# @app.route("/about/<username>")
# def about(username):
#     return f'<h1>This is the about page of {username}</h1>'


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()

    if form.validate_on_submit():
        user_to_create = User(username=form.username.data, email_address=form.email_address.data, password_hash=form.password1.data)

        db.session.add(user_to_create)
        db.session.commit()

        return redirect(url_for('market'))

    return render_template('register.html', form=form)