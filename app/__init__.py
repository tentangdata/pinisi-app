# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask.ext.sqlalchemy import SQLAlchemy

# Import Heroku
from flask.ext.heroku import Heroku

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Heroku
# heroku = Heroku(app)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable
from app.landing.controllers import landing
from app.maps.controllers import maps
app.register_blueprint(landing)
app.register_blueprint(maps)