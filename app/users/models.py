
from flask_login import UserMixin

from app.database import db, CRUDMixin
from app.extensions import bcrypt



class User(CRUDMixin, UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  team_number = db.Column(db.Integer, unique=True, nullable=False)
  username = db.Column(db.String(60), unique=True, nullable=False)
  password_hash = db.Column(db.String, nullable=False)
  is_admin = db.Column(db.Boolean())

  def __init__(self, password, **kwargs):
    super(User, self).__init__(**kwargs)
    self.set_password(password)

  def __repr__(self):
    return f"<User {self.id}:{self.team_number} - {self.username}>"

  def set_password(self, password):
    self.password_hash = bcrypt.generate_password_hash(password, 10).decode('utf-8')

  def check_password(self, password):
    return bcrypt.check_password_hash(self.pw_hash, password)