from todoapp import app, urls
from gevent import monkey;
from gevent.wsgi import WSGIServer

if __name__ == "__main__":
    print "GEvent Started"
    monkey.patch_all()
    http_server = WSGIServer(('',8000), app)
    http_server.serve_forever()

# if __name__ == "__main__":
# 	app.debug = True
# 	app.run(host=app.config['HOST'], port=app.config['PORT'])

