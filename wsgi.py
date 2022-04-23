from werkzeug import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware

from apis.messaging.views import message_blueprint
from apis.health_check import health_blueprint
from master.app import app

app.register_blueprint(message_blueprint)
app.register_blueprint(health_blueprint)


application = DispatcherMiddleware(app, {
    '/messaging': app
})


if __name__ == '__main__':
    run_simple('0.0.0.0', 8000, application, use_debugger=False, use_reloader=True, threaded=True)