
from flask_login import login_required

from app.users import users



@users.route("/create")
@login_required
def create_user():
  pass
  # form = CreateUserForm()
  # if form.validate_on_submit():