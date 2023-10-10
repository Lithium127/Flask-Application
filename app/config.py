

class BaseConfig(object):
  SITE_NAME = "CORE 2062 Scouting"
  SECRET_KEY = "SOMETHING SNEAKY"
  SQLALCHEMY_DATABASE_URI = "sqlite:///site_test.db"


class DevConfig(BaseConfig):
  SECRET_KEY = "DEVELOPMENT"