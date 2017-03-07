from flask import Flask, render_template, request

from models.todo import *

app = Flask(__name__) # create the application instance :)


@app.route("/ajaxKit/<action>", methods=['GET', 'POST'])
def ajaxKit(action):
    """
    :param action: name of action
    :return: rendered temlate
    """

    todo_list = Todo()

    if action == 'add_item':
        if request.method == 'POST':
            if request.form['add_new_item']:

                item = request.form['add_new_item']

                return render_template('ajaxKit.html', item=todo_list.add_item_to_list(item), action='add_new')

    if action == 'toggle': #change status of item in db
        if request.method == 'POST':

            toggle_id = request.form['toggle_id']
            todo_list.toggle(toggle_id)

            return render_template('ajaxKit.html', action='toggle')

    if action == 'remove':  # remove list from db
        if request.method == 'POST':
            remove_id = request.form['remove_id']
            todo_list.remove(remove_id)

            return render_template('ajaxKit.html', action='remove')

    if action == 'update':  # update item
        if request.method == 'POST':
            item_id = request.form['item_id']
            text_update = request.form['text_update']

            return render_template('ajaxKit.html', item=todo_list.update(item_id, text_update), action='update')


@app.route("/", methods=['GET', 'POST'])
def index():
    """home page"""
    todo_list = Todo()
    return render_template('index.html', items=todo_list.get_full_list(), method=request.method)

if __name__ == "__main__":
    app.run(debug=True)