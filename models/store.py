from db import db

class StoreModel(db.Model):
    __tablename__ = "stores"
    id = db.Column(db.Integer, primary_key = True)  
    name = db.Column(db.String(30))
    items = db.relationship("ItemModel", lazy = "dynamic")   #Note:  "lazy = "dynamic"" is added to reduce the operation expenses every time we create StoreModel
    
    def __init__(self, name):
        self.name = name

    def json(self):
        return {"name": self.name, "items": [item.json() for item in self.items.all()]}  #It was "return {"name": self.name, "item": [self.items]}",   #Note: ".all()" is added because "lazy = "dynamic"" in items variable

    @classmethod
    def find_by_name(cls, name): 
        return cls.query.filter_by(name = name).first()  

    def save_to_db(self):  
        db.session.add(self) 
        db.session.commit()

    def delete_from_db(self): 
        db.session.delete(self)  
        db.session.commit()