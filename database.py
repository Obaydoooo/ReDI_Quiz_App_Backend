
import certifi as certifi
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from pymongo import MongoClient
from fastapi import FastAPI
from bson import ObjectId
from starlette import status

CONNECTION_STR = "mongodb+srv://Redi:O_1234@cluster0.oowbj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"

# setup database connection
connection = MongoClient(CONNECTION_STR, tlsCAFile=certifi.where())

# connect to database
db = connection.projectTest

quizzes_collection = db.Quiz




