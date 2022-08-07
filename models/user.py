#import sqlite3   #No need for "import sqlite3" now
from db import db


class UserModel(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(30))

    def __init__(self, username, password):  #It was "__init__(self, _id, username, password)"
        #self.id = _id  #No need fo id since it is auto-incrementing we made it like "__init__" in ItemModel
        self.username = username
        self.password = password


    @classmethod
    def find_by_username(cls, username):   #Note: it was "def find_by_username(self, username)"
        return cls.query.filter_by(username = username).first()  #Note: we can say "query.filter_by(name = name).filter_by(id= id)filter_by(price= price)", #Note: ".first()" return the first row only, #Note: "return ItemModel.query.filter_by(name = name).first()" return a model object not dictionary, #Note: "return ItemModel.query.filter_by(name = name).first()" can be "return cls.query.filter_by(name = name).first()"
       
        """    #No need for this block since we have sqlalchemy
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username = ?"
        result = cursor.execute(query, (username,))

        row = result.fetchone()  #This will get the first row from the "result" list
        if row:  #originally "if row is not None"
            user = cls(*row)   #Note: it was "user = User(row[0], row[1], row[2])"
        else:
            user = None  #shouldn't we show a message that "user is not found" ot something ?
        connection.close()   #None: we didn't add connection.commit() since we didn't add any data to the database
        return user
        """
    
    @classmethod
    def find_by_id(cls, _id):   #Note: it was "def find_by_username(self, username)"
        return cls.query.filter_by(id = _id).first()   #Note: the first id in "(id = _id)" is the clumn name and the second in the input, argument, variable name

        """  #No need for this block since we have sqlalchemy
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id = ?"
        result = cursor.execute(query, (_id,))

        row = result.fetchone()  #This will get the first row from the "result" list
        if row:  #originally "if row is not None"
            user = cls(*row)   #Note: it was "user = User(row[0], row[1], row[2])"
        else:
            user = None  #shouldn't we show a message that "user is not found" ot something ?
        connection.close()   #None: we didn't add connection.commit() since we didn't add any data to the database
        return user
        """

    def save_to_db(self):   
        db.session.add(self)  
        db.session.commit()

