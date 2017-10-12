import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
from flask_login import LoginManager, login_required, login_user
from config import app_config
from init import create_app
from forms import LoginForm

config_name = os.getenv('APP_SETTINGS', 'development')
app = create_app(config_name)

client = MongoClient(
    os.environ['DB_PORT_27017_TCP_ADDR'],
    27017)
db = client.tododb

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"



@app.route('/')
@login_required
def todo():

    _items = db.tododb.find()
    items = [item for item in _items]

    return render_template('todo.html', items=items)


@app.route('/new', methods=['POST'])
def new():

    item_doc = {
        'name': request.form['name'],
        'description': request.form['description']
    }
    db.tododb.insert_one(item_doc)

    return redirect(url_for('todo'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flash('Logged in successfully.')

        next = request.args.get('next')
        # is_safe_url should check if the url is safe for redirects.
        # See http://flask.pocoo.org/snippets/62/ for an example.
        if not is_safe_url(next):
            return abort(400)

        return redirect(next or url_for('index'))
    return render_template('login.html', form=form)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)