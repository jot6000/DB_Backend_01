from fastapi import FastAPI
from pydantic import BaseModel
from pymongo import MongoClient

client = MongoClient()
db = cleint["reprimandApp"]
rep_collection = db["reprimands"]

app = FastAPI()

class Reprimand(BaseModel):
    studentId: str
    staffName: str
    date: str
    time: str
    contactType: str
    contactReason: str
    details: str
    executed: bool

@app.post("/reprimand")
async def addReprimand(rep: Reprimand):
    """Used to add reprimands to the database"""
    result = rep_collection.insert_one(rep.dict)
    return { "insertion" : result.acknowledged }

@app.get("/reprimand/nonExecuted")
async getNonExecuted()
    ""Retrieves all non executed reprimands"""
    repList = rep_collection.find({ "executed" : False })
    return [ Reprimand(**rep) for rep in repList]