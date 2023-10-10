
from flask.cli import with_appcontext

import click

from app.database import db
from app.users.models import User

@click.command("init-db")
@with_appcontext
def init_db():
  """Creates the database used for the server"""
  db.create_all()


@click.command("create-user")
@click.argument("username", required=True)
@click.argument("password", required=True)
@click.argument("teamnum", required=True)
def create_user(username, password, teamnum):
  User.create(
    password = str(password),
    username = str(username),
    team_number = int(teamnum)
  )