import os

class BaseConfig(object):
  SITE_NAME = os.environ.get("SITE_NAME", "Core 2062")
  SECRET_KEY = os.environ.get("SECRET_KEY", "Secrets")
  SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI","sqlite:///site_test.db")


class DevConfig(BaseConfig):
  SECRET_KEY = "DEVELOPMENT"