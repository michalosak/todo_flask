from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

from models.todoalchemy import *


@app.route("/ajaxKit/<action>", methods=['GET', 'POST'])
def ajaxKit(action):
    """
    :param action: name of action
    :return: rendered temlate
    """


    if action == 'add_item':
        if request.method == 'POST':
            if request.form['add_new_item']:

                item = request.form['add_new_item']
                new_item = Todos(item)
                db.session.add(new_item)
                db.session.commit()
                newitem = Todos.query.filter_by(ID=new_item.ID).first()

                return render_template('ajaxKit.html', item=newitem, action='add_new')

    if action == 'toggle': #change status of item in db
        if request.method == 'POST':
            print(request.form['toggle_id'])
            toggle_id = request.form['toggle_id']
            db.session.execute("UPDATE `todo_items` SET `status` =  (CASE `status` WHEN 0 THEN 1 WHEN Null THEN 1 ELSE 0 END) WHERE ID=:val", {'val': toggle_id})
            db.session.commit()
            return render_template('ajaxKit.html', action='toggle')

    if action == 'remove':  # remove list from db
        if request.method == 'POST':

            Todos.query.filter_by(ID=request.form['remove_id']).delete()

            return render_template('ajaxKit.html', action='remove')

    if action == 'update':  # update item
        if request.method == 'POST':
            item_id = request.form['item_id']
            todo_item = Todos.query.filter_by(ID=item_id).first()
            update_text = request.form['text_update']
            todo_item.item_title = update_text

        return render_template('ajaxKit.html', item=todo_item, action='update')


@app.route("/", methods=['GET', 'POST'])
def index():
    """home page"""
    return render_template('index.html', items=Todos.query.all(), method=request.method)

if __name__ == "__main__":
    app.run(debug=True)
