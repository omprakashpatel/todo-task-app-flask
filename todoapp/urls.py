from todoapp import app
from flask import request, jsonify, redirect, render_template, url_for
from handlers import *

@app.route('/')
def index():
	return redirect(url_for('task_api'))
	return render_template('index.html')


@app.route('/create_task', methods=['GET', 'POST'])
def create_task_api():
	if request.method == "GET":
		return render_template('create_task.html')
	elif request.method == "POST":
		data = create_task(**(request.form or {}))
		return redirect(url_for('task_api'))


@app.route('/task', methods=['GET'])
def task_api():
	if request.method == "GET":
		return render_template('tasks.html', tasks=get_all_task())
	else:
		return "Invalid Request Method"


@app.route('/task/<task_id>', methods=['GET', 'POST'])
def task_id_api(task_id):
	if request.method == "GET":
		return render_template('task_desc.html',
			task=get_task(task_id=task_id))
	elif request.method == "POST":
		data = update_task(task_id=task_id, **(request.form or {}))
		return render_template('task_desc.html',
			task=get_task(task_id=task_id))

@app.route('/task/<task_id>/edit', methods=['GET'])
def update_task_api(task_id):
	print "update_task_api"
	if request.method == "GET":
		return render_template('task_edit.html',
				task=get_task(task_id=task_id),
				tags=get_all_tags())

@app.route('/search', methods=['GET'])
def search_api():
	if request.method == "GET":
		tasks = search_tag(**(request.args or {}) )
		return render_template('tasks.html', tasks=tasks)
	else:
		return "Invalid Request Method"

@app.errorhandler(404)
def page_not_found(error):
	return "<div><h2>Page Not Found </h2></div>", 404

@app.errorhandler(Exception)
def exception_handler(error):
    print "**************************"
    print str(error)
    print "**************************"
    return str(error)
