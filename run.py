from app import app
from db import db

db.init_app(app)

@app.before_first_request
def create_tables():  #Very important note: this method create tables that sees only if we do not import "Store, StoreList" then it will not create its tables
    db.create_all()   #This method will create this database "sqlite:///data.db" and all tables of it unless it is already exist so no need for "create_tables.py" but it cause slowleness in the register,post,put (maybe get) verbs
