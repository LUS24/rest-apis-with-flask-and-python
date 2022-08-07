from flask import Flask
from flask_restful import Api
#from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db



app = Flask(__name__)
api = Api(app)
app.secret_key = "key"
#jwt = JWT(app, authenticate, identity)  #/auth
app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["SQLALCHEMY_TRACK_MODEFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"


'''
class Student(Resource):
    def get(self, name):
        return {"student": name}

api.add_resource(Student, "/student/<string:name>")
'''

api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":
    db.init_app(app)
    app.run(port = 5000, debug= True)