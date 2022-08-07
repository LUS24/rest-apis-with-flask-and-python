#import sqlite3  #No need for it since we have sqlalchemy
from flask_restful import Resource, reqparse
from models.item import ItemModel



class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("price", 
    type= float, 
    required = True,
    help = "price field cannot be blank"
    )
    parser.add_argument("store_id", 
    type= int, 
    required = True,
    help = "store_id field cannot be blank for this item"
    )

    def get(self, name):
        item = ItemModel.find_by_name(name) 
        if item:
            return item.json()  #Very important note: we change "find_by_name" function to return object instead of dictionary so it was "return item" and we added ".json()" to make it return dict
        return {"message": "item was not found"}, 404
        
    def post(self, name):
        if ItemModel.find_by_name(name):  
            return {"message": "item '{}' is already exists".format(name)}, 400
        data = Item.parser.parse_args()
        item = ItemModel(name, **data)  #It was dict "item = {"name": name, "price": data["price"]}", then "ItemModel(name, data["price"], data["store_id"])"
        try:
            item.save_to_db()  #It was "ItemModel.insert(item)" ten "item.insert() "
        except:
            return {"message": "An error occued inserting the item"}, 500
        return item.json(), 201    #It was "return item, 201"
        
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
            return {"message": "item deleted successfully"}
        return {"message": "item wanted to be deleted doesn't exist"}, 404 
        """
        if ItemModel.find_by_name(name):
            connection = sqlite3.connect("data.db")
            cursor = connection.cursor()
            query = "DELETE FROM items WHERE name = ?"   
            cursor.execute(query, (name,))
            connection.commit()
            connection.close()  
            return {"message": "item deleted successfully"}  
        return {"message": "item wanted to be deleted doesn't exist"}, 404  
        """
    
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        #updated_item = ItemModel(name, data["price"])  #It was "{"name": name, "price": data["price"]}" then no need for it since we have "save_to_db"
        if item is None:
            item = ItemModel(name, **data)  #It was "ItemModel(name, data["price"], data["store_id"])"
            #updated_item.save_to_db()  #It was "ItemModel.insert(updated_item)" then "updated_item.insert()" then no need for it since we have "save_to_db"
            print("item didin't exist but inserted successfully")
        else:
            item.price = data["price"]  #Very important note: since every item has a unique id we can use the same variable "item" and no need for "updated_item"
            #updated_item.save_to_db()  #It was "ItemModel.update(updated_item)" then "updated_item.update()" then no need for it since we have "save_to_db"
            item.store_id = data["store_id"]
            print("item exist but updated successfully")
        item.save_to_db()
        return item.json()  #It was "updated_item" then "updated_item.json()"

class ItemList(Resource):
    def get(self):
        return {"items": [item.json() for item in ItemModel.query.all()]}   #Another way to do it "return {"items": list(map(lambda x: x.json(), ItemModel.query.all()))}" and some say it is faster thant the other way
        

        """  #This is my solution for the line above in return
        all_items = ItemModel.query.all()
        items = []
        for item in all_items:
            items.append(item.json())
        return items
        """

        """  #We are using sqlalchemy now
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({"name": row[0], "price": row[1]})
        connection.close() 
        return {"items": items}
        """



#Very important note: if you didn't include the store_id in the postman you will get error like:
#{
#    "message": {
#        "store_id": "store_id field cannot be blank"
#    }
#}