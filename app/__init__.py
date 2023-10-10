__VERSION__ = "0.0.3"

from flask import Flask, render_template

from app import config


from app.extensions import (
  lm,
  migrate,
  bcrypt
)
from app.commands import (
  init_db,
  create_user
)
from app.database import db

from app.auth import auth
from app.users import users


def create_app(config=config.DevConfig):

  app = Flask(__name__)
  app.config.from_object(config)

  reg_extensions(app)
  reg_blueprints(app)
  
  
  @app.route("/")
  def index():
    return "Index"
  
  return app


def reg_extensions(app):
  db.init_app(app)
  migrate.init_app(app, db)
  
  lm.init_app(app)
  bcrypt.init_app(app)

def reg_blueprints(app):
  app.register_blueprint(users, url_prefix="/users")
  app.register_blueprint(auth, url_prefix="/auth")

def reg_commands(app):
  app.cli.add_command(init_db)
  app.cli.add_command(create_user)