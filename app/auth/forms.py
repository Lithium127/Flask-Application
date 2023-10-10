from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired

from app.users.models import User

class LoginForm(FlaskForm):
  username = StringField("Username", validators=[DataRequired()])
  password = PasswordField("Password", validators=[DataRequired()])

  def __init__(self, *args, **kwargs):
    FlaskForm.__init__(self, *args, **kwargs)
    self.user = None

  def validate(self):
    rv = FlaskForm.validate(self)

    if not rv:
      return False

    self.user = User.query.filter_by(username=self.username.data).first()

    if not self.user:
      self.username.errors.append('Unknown username')
      return False

    if not self.user.check_password(self.password.data):
      self.password.errors.append('Incorrect Password')
      return False

    return True