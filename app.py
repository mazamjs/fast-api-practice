from fastapi import FastAPI
import json
app = FastAPI()

def load_data():
    with open("data.json","r")as f:
        data = json.load(f)
        return data

def save_data(data):
    with open("data.json","w")as f:
        json.dump(data,f, indent=4)
@app.get("/engineer")
def first_api():
    return {"message": "Hello world"}

@app.get("/view")
def view_api():
     load = load_data()
     return {"message": "This is the view endpoint", "data" : load}

@app.get("/single/{id}")
def single_api(id: str):
    load = load_data()
    if id in load:
        return load[id]        
    return {"message": "Data not found"}

@app.post("/add")
def add_api(id:str, new_data: dict):
    load = load_data()
    if id in load:
        return {"message": "Ya id exist karti hay!"}
    load[id] = new_data
    save_data(load)
    return {
        "message": "Data added successfully",
        "unique_id": id,
        "data": new_data
    }

@app.put("/update/{id}")
def update_data(id:str, update_data: dict):
    load = load_data()
    if id not in load:
        return {"message" : "id not found in the data"}
    load[id] = update_data
    save_data(load)
    return {
        "message": "Data updated successfully",
        "patient_id": id,
        "patient_data": load[id]            
    }

@app.delete("/delete/{id}")
def delete_data(id:str):
    load = load_data()
    if id not in load:
        return {"message": "id not found in the data"}
    deleted_data = load[id]
    del load[id]
    save_data(load)
    return{
        "message": "Data deleted successfully",
        "deleted_id": id,
        "deleted_data": deleted_data
    }
    