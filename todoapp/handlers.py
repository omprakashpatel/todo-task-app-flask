
from todoapp.models import Task, Tag

def create_task(title, desc, tags, **kwargs):
	"""
		Handler is FOr creating Task
	"""
	if isinstance(title, list):
		title = title[0]
	if isinstance(desc, list):
		desc = desc[0]
	if isinstance(tags, list):
		tags = tags[0]
	if tags:
		tags = map(lambda x: x.strip(), tags.split(','))
		for _tag in tags:
			create_tag(_tag)

	try:
		_task = Task(title=title, desc=desc, tags=tags)
		_id = _task.save()
	except Exception, e:
		raise e

	return "Task Created"

def get_all_task(**kwargs):
	tasks = []
	for _task in Task.objects:
		tasks.append({'id': _task.id,
					'title': _task.title,
					'desc': _task.desc,
					'tags': _task.tags})
	return tasks


def get_task(task_id, **kwargs):
	try:
		task = Task.objects.get(id=task_id)
	except Exception, e:
		raise e
	return {'id': task.id,
			'title': task.title,
			'desc': task.desc,
			'tags': task.tags
	}


def update_task(task_id, title, desc, tags=[], **kwargs):
	if isinstance(title, list):
		title = title[0]
	if isinstance(desc, list):
		desc = desc[0]
	if tags and not isinstance(tags, list):
		tags = tags
	try:
		task = Task.objects.get(id=task_id)
		task.title = title
		task.desc = desc
		task.tags = tags
		task.save()
	except Exception, e:
		raise e
	return "Updated"


# ======================================

def create_tag(tag):
	try:
		_tag = Tag()
		_tag.id = tag
		_tag.save()
	except Exception, e:
		print str(e)
	return _tag.id


def get_all_tags():
	return [_tag.id for _tag in Tag.objects]


def search_tag(tag):
	if isinstance(tag, list):
		tag = tag[0]
	task = Task.objects.search_text(tag)
	tasks = []
	for _task in task:
		tasks.append({'id': _task.id,
					'title': _task.title,
					'desc': _task.desc,
					'tags': _task.tags})
	return tasks
