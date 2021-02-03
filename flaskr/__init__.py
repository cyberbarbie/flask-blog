import os
from flask import Flask

# __init__.py - contains the app factory and tells Python that flaskr dir should be treated as a package

# app factory function
def create_app(test_config=None):
    # create & configure the app
    # creates the Flask instance
    app = Flask(__name__, instance_relative_config=True)
    # sets some default configs 
    app.config.from_mapping(
        # keeps data safe
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    from . import db
    db.init_app(app)

    # views to register new users to log in nd out 
    from . import auth
    app.register_blueprint(auth.bp)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple route that says hello
    @app.route('/')
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app