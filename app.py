from flask import Flask,request

app = Flask(__name__)


stores = [
    {
        "name" : "MyStore",
        "items":[
            {
                  "name" : "chair",
            "prince": 15.99
            }
        ]
    }
]


@app.get("/stores")
def get_stores():
    return {"stores":stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name":request_data["name"],"items":[]}
    stores.append(new_store)
    return new_store , 201


@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name":request_data["name"],"price":request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message":"Store Not found"}, 404

@app.get("/store/<string:name>")
def get_store_by_name(name: str):
    for store in stores:
        if store["name"] == name:
            return store
    # raise HTTPException(status_code=404, detail="Store not found")
    return {"message":"Store Not Found"}, 404

if __name__ == "__main__":
    app.run()