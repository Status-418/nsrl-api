from flask import Flask

def _initialize_blueprints(application):
    '''
    Register Flask blueprints
    '''
    from app.views.nsrl import nsrl
    application.register_blueprint(nsrl, url_prefix='/api/v1/nsrl')

def create_app():
    '''
    Create an app by initializing components.
    '''
    application = Flask(__name__)

    _initialize_blueprints(application)

    # Do it!
    return application
