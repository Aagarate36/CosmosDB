from fastapi import FastAPI, HTTPException
from azure.cosmos import exceptions
from database import container 

app = FastAPI (title="CRUD FastAPI")

#cosmosdb.com/products --> crear productos
#cosmosdb.com/products/1 --> obtiene productos 1
#cosmosdb.com/products --> Listar productos (GET)
# 

@app.get("/")
def home():
    return "Mi primera api con FastAPI"
