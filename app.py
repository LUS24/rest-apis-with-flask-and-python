from flask import Flask
from flask_restful import Api
#from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
#from db import db
import os



app = Flask(__name__)
api = Api(app)
app.secret_key = "key"
#jwt = JWT(app, authenticate, identity)  #/auth
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["SQLALCHEMY_TRACK_MODEFICATIONS"] = False

uri = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
app.config['SQLALCHEMY_DATABASE_URI'] = uri

"""  #Note: the four lines above is to replace these lines since it causes problems in Heroku taken from QA
#app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///data.db")  #It was "app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db""
#Note: "os.environ.get("DATABASE_URL", "sqlite:///data.db")" if heroku database postgres didn't work for any reason, then the local sqlite3 will do.
uri = os.getenv("DATABASE_URL")  #The line "app.config["SQLALCHEMY_DATABASE_URI"]" is remove because it causes problem in Heroku deployment and according to him it should be removed and the following 4 lines 
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
# rest of connection code using the connection string `uri`
"""


api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    db.init_app(app)  #I got this line outside the if statement because i faced an issue with heroku and one of the students mention that he solved the issue by this way
    app.run(port = 5000, debug= True)

"""  #This block because i faced an issue with heroku so i accessed his "app.py" file to find these lines exist.
    if app.config["DEBUG"]:
        @app.before_first_request
        def create_tables():
            db.create_all()
"""




    