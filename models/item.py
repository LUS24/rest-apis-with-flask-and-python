#import sqlite3   #No need for "import sqlite3" now
from db import db

class ItemModel(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key = True)  #Quest: our item "__init__" function doesn't have "id" property like users "__init__" function, Ans: it will be inserted but will not be used and i have added id column in the items database in "create_tables.py"
    name = db.Column(db.String(30))
    price = db.Column(db.Float(precision = 2))
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))   #Note: "stores.id" means the stores table, the id columns
    store = db.relationship('StoreModel')
    
    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    @classmethod
    def find_by_name(cls, name): 
        return cls.query.filter_by(name = name).first()  #Note: we can say "query.filter_by(name = name).filter_by(id= id)filter_by(price= price)", #Note: ".first()" return the first row only, #Note: "return ItemModel.query.filter_by(name = name).first()" return a model object not dictionary, #Note: "return ItemModel.query.filter_by(name = name).first()" can be "return cls.query.filter_by(name = name).first()"
        #Quest: what if the item is not in the database what "ItemModel.query.filter_by" will return ?
        """ #We now use SQLALCHEMY instead of sqlite
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM items WHERE name = ?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()
        if row:    
            return cls(*row)    #It was "return {"item": {"name": row[0], "price": row[1]}}" to make it return object instead of dict then it became "return cls(row[0], row[1]"
        """
    #@classmethod
    def save_to_db(self):   #It was "def insert(cls, item) then def insert(self)"  #Note: "save_to_db(self)" do the job of "insert" and "update" functions   #Quest: i didn't understand why "save_to_db" replaces "inser" and "update"
        db.session.add(self)  #Quest: he said we can add multiple session objects then commit it how the way is it "db.session.add(self, object2)" or after "db.session.add(self)" we add "db.session.add(object2)" ?
        db.session.commit()
        """
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (?, ?)"
        cursor.execute(query, (self.name, self.price))  #It was "cursor.execute(query, (item["name"], item["price"]))"
        connection.commit()
        connection.close()
        """
    """  #No need for this function since "def save_to_db(self)" will do the job
    #@classmethod
    def update(self):   #It was "def update(cls, item):"
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "UPDATE items SET price = ? WHERE name = ?"   
        cursor.execute(query, (self.price, self.name))  #Very important note: it is ok to say (self.name, self.price) too since the name will go to name and price will go to price
        connection.commit()
        connection.close() 
    """

    def delete_from_db(self): 
        db.session.delete(self)  
        db.session.commit()