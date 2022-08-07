import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel



class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", 
    type= str, 
    required = True,
    help = "username field cannot be blank"
    )
    parser.add_argument("password", 
    type= str, 
    required = True,
    help = "password field cannot be blank"
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data["username"]):    #It is originally "if User.find_by_username(data["username"]) is not None:"
            return {"message": "this username already registred"}, 400

        user = UserModel(**data)   #It was "UserModel(data["username"], data["password"])", #Quest: what is the difference between "**data" and "*data" ?
        user.save_to_db()
        return {"message": "user created successfully"}, 201


        """  #We now use SQLALCHEMY instead of sqlite
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)"  #Note: the id has "NULL" because it is auto-incrementing we don't need to assign a value
        cursor.execute(query, (data["username"], data["password"],))  #Note: no need for the comma after "data["password"]"

        connection.commit()
        connection.close()
        return {"message": "user created successfully"}, 201
        """