
from flask import render_template, redirect, url_for, request, flash

from flask_login import login_required, logout_user, login_user

from app.auth import auth
from app.extensions import lm
from app.users.models import User

from .forms import LoginForm

@lm.user_loader
def load_user(id):
  return User.get_by_id(int(id))

@auth.route("/login", methods=['GET','POST'])
def login():
  form = LoginForm() # flask_wtf form
  if form.validate_on_submit():
    login_user(form.user)
    flash(
      f"Logged in as Team {User.query.filter_by(username=form.username.data).first().team_number}",
      "success"
    )
    return redirect(request.args.get('next') or url_for('index'))
  return render_template("login.html", form=form)


@auth.route("/logout", methods=['GET'])
@login_required
def logout():
  logout_user()
  flash(
    "Logged out successfully",
    "success"
  )
  return redirect(url_for('index'))