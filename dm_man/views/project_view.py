import sys
from . import *
from ..models.user import User, UserQuery
from ..models.project import Project

@app.route('/projects')
def projects():
    projects = Project.query.all_projects()
    users = User.query.all_users()

    return render_template('project_admin.html', projects=projects, navigation=navigation, users=users)

@app.route('/projects/new', methods=['POST'])
def new_project():
    usr = User.query.get(request.form['Owner'])
    item_doc = Project(Name=request.form['Name'], Owner=usr)
    item_doc.save()

    return redirect(url_for('projects'))

@app.route('/projects/delete/<id>')
def delete_project(id):
    item = Project.query.get(id)
    item.remove()
    return redirect(url_for('projects'))

@app.route('/projects/edit/<id>')
def edit_project(id):
    item = Project.query.get(id)
    users = User.query.all_users()
    return render_template('project_edit.html', item=item, navigation=navigation, users=users)

@app.route('/projects/edit/<id>', methods=['POST'])
def update_project(id):
    item = Project.query.get(id)
    item.Name = request.form['Name']
    item.Owner = User.query.get(request.form['Owner'])
    item.save()

    return redirect(url_for('projects'))
