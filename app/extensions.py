from flask_login import LoginManager
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


lm = LoginManager()
migrate = Migrate()
bcrypt = Bcrypt()