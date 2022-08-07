from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):

    def get(self, name):
        store = StoreModel.find_by_name(name) 
        if store:
            return store.json()  
        return {"message": "store was not found"}, 404
        
    def post(self, name):
        if StoreModel.find_by_name(name):  
            return {"message": "store '{}' is already exists".format(name)}, 400
        store = StoreModel(name) 
        try:
            store.save_to_db()  
        except:
            return {"message": "An error occued creating the store"}, 500
        return store.json(), 201  
        
    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
            return {"message": "store deleted successfully"}
        return {"message": "store wanted to be deleted doesn't exist"}, 404 
    

class StoreList(Resource):
    def get(self):
        return {"items": [store.json() for store in StoreModel.query.all()]}  