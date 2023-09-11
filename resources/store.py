from flask.views import MethodView
from flask_smorest import abort,Blueprint
from models import StoreModel
from sqlalchemy.exc import SQLAlchemyError,IntegrityError

from schemas import StoreSchema
from db import db

blp =Blueprint("stores",__name__,description="Operations on stores")

@blp.route("/store/<int:store_id>")
class Store(MethodView):
    @blp.response(200,StoreSchema)
    def get(self,store_id):
      return StoreModel.query.get_or_404(store_id)

    def delete(self,store_id):
        store =  StoreModel.query.get(store_id)
        db.session.delete(store)
        db.session.commit()
        return {"message":"Item Deleted."}

@blp.route("/store")
class StoreList(MethodView):
    @blp.response(200,StoreSchema(many=True))
    def get(self):
        return StoreModel.query.all()

    @blp.arguments(StoreSchema)
    @blp.response(200,StoreSchema)
    def post(self,store_data):
       store = StoreModel(**store_data)

       try:
           db.session.add(store)
           db.session.commit()
       except IntegrityError:
           abort(400,message="A Store with that name already exists.")
       except SQLAlchemyError:
           abort(500,message="An Error occured while inserting ...")

       return store

    def delete(self):
        all_stores = StoreModel.query.all()
        for store in all_stores:
            db.session.delete(store)

        db.session.commit()
        return{"message":"All Stores are deleted !"}