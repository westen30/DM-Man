from . import *
from ..models.user import User, UserQuery


@app.route('/user')
def users():

    items = User.query.all_users()

    return render_template('user_admin.html', items=items, navigation=navigation)


@app.route('/user/new', methods=['POST'])
def new():

    item_doc = User(Name=request.form['Name'], Role=request.form['Role'])
    item_doc.save()

    return redirect(url_for('users'))

@app.route('/user/delete/<id>')
def delete(id):
    item = User.query.get(id)
    item.remove()
    return redirect(url_for('users'))

@app.route('/user/edit/<id>')
def edit_user(id):
    item = User.query.get(id)
    return render_template('user_edit.html', item=item, navigation=navigation)

@app.route('/user/edit/<id>', methods=['POST'])
def update_user(id):
    item = User.query.get(id)
    item.Name = request.form['Name']
    item.Role = request.form['Role']
    item.save()

    return redirect(url_for('users'))
