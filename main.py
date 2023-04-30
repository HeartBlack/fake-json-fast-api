from fastapi import FastAPI
app = FastAPI()



fake_database = {
    1:{
        "name":"Ramesh",
        "age":25
    },
    2:{
        "name":"Suresh",
        "age":30

    },
    3:{
        "name":"Rohan",
        "age":35

    },
    4:{
        "name":"Rakesh",
        "age":40

    },
    5:{
        "name":"Anajan",
        "age":45

    },

}

@app.get("/")
def getItems():
    return fake_database


@app.get("/{id}")
def getItem(id:int):
    return fake_database[id]


@app.post("/")
def addItem(name:str,age:int):
    newId = len(fake_database.keys()) + 1
    fake_database[newId] = {"name":name,"age":age}
    return fake_database

@app.put("/{id}")
def updateItem(id:int,name:str,age:int):
    fake_database[id]['name'] = name
    fake_database[id]["age"] = age
    return fake_database

@app.delete("/{id}")
def deleteItem(id:int):
    del fake_database[id]
    return fake_database