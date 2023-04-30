from fastapi import FastAPI

app = FastAPI()


fake_database = {
    1: {"name": "Ramesh", "age": 25},
    2: {"name": "Suresh", "age": 30},
    3: {"name": "Rohan", "age": 35},
    4: {"name": "Rakesh", "age": 40},
    5: {"name": "Anajan", "age": 45},
}


@app.get("/")
def getitems():
    """
    Function: getItems

    Parameters: None

    Return: The fake_database containing all data

    Description: This function retrieves all data from the Fake Database.
    """
    return fake_database


@app.get("/{id}")
def getitem(item_id: int):
    """
        Function: getItem

    Parameters:

        id (int): The unique identifier of the item to be retrieved

    Return: The item with the specified id from the fake_database

    Description: This function retrieves an item from the Fake Database by its id.
    """
    return fake_database[item_id]


@app.post("/")
def additem(name: str, age: int):
    """
    Function: addItem

    Parameters:

        name (str): The name of the item to be added
        age (int): The age of the item to be added

    Return: The updated fake_database containing the new item

    Description: This function adds a new item to the Fake Database."""
    new_id = len(fake_database.keys()) + 1
    fake_database[new_id] = {"name": name, "age": age}
    return fake_database


@app.put("/{id}")
def updateitem(item_id: int, name: str, age: int):
    """
        Function: updateItem

    Parameters:

        id (int): The unique identifier of the item to be updated
        name (str): The new name for the item
        age (int): The new age for the item

    Return: The updated fake_database containing the updated item

    Description: This function updates an existing item in the Fake Database.
    """
    fake_database[item_id]["name"] = name
    fake_database[item_id]["age"] = age
    return fake_database


@app.delete("/{id}")
def deleteitem(item_id: int):
    """
    Function: deleteItem

    Parameters:

        id (int): The unique identifier of the item to be deleted

    Return: The updated fake_database without the deleted item

    Description: This function deletes an item from the Fake Database by its id."""
    del fake_database[item_id]
    return fake_database
