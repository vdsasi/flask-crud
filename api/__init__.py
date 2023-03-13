from flask import Flask
from .views import views
from .auth import auth 

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'jsdjflkajakffljeifjaiew'

    app.register_blueprint(views, path='/')
    app.register_blueprint(auth, path='/')
    
    return app
