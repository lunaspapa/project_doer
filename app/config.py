import os

class Config:
  SQLALCHEMY_DATABASE_URI = (
    f"postgresql://doer_dev:missTheRage@localhost/project_doer"
  )
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SECRET_KEY = "1m155th3r4ge"
