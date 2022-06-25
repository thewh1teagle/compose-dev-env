import fastapi
import uvicorn
import os
import pymongo

MONGO_URI = os.getenv("MONGODB_URL")
APP_PORT = os.environ.get('PORT', '8000')
app = fastapi.FastAPI()

# test mongo connection
myclient = pymongo.MongoClient(MONGO_URI)
mydb = myclient["mydatabase"]
mycol = mydb["mycollection"]
mydict = { "hello": "world" }
x = mycol.insert_one(mydict)
print(f'inserted {x.inserted_id} into mongo')


@app.get("/")
def root():
    return {"message": "Hello World!"}



if __name__ == "__main__":
    print(f'Starting FastAPI server on port {APP_PORT}')
    uvicorn.run(app, host="0.0.0.0", port=APP_PORT)
    