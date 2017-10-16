from flask import render_template, redirect, request, url_for
from flask_login import LoginManager, login_required
from .dm import app, db
from .models.user import User, UserQuery

''' login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login" '''

#db = client.newdb

@app.route('/')
def todo():

    items = User.query.all_users()
    #items = [item for item in _items]

    return render_template('user_admin.html', items=items)


@app.route('/new', methods=['POST'])
def new():

    item_doc = User(Name = request.form['Name'], Role = request.form['Role'])
    item_doc.save()

    return redirect(url_for('todo'))

@app.route('/delete/<id>')
def delete(id):
    item = User.query.get(id)
    item.remove()
    return redirect(url_for('todo'))

@app.route('/edit/<id>')
def edit_user(id):
    item = User.query.get(id)
    return render_template('user_edit.html', item=item)

@app.route('/edit/<id>', methods=['POST'])
def update_user(id):
    item = User.query.get(id)
    item.Name = request.form['Name']
    item.Role = request.form['Role']
    item.save()

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