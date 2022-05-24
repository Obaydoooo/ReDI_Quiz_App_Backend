from starlette import status
from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter
from database import quizzes_collection
from quizzes_model import all_quizzes, QuizCreator

app_routers = APIRouter()


@app_routers.get("/")
def root():
    return {"WELCOME"}


@app_routers.get("/quizzes")
def get_quizzes():
    return all_quizzes(quizzes_collection.find())


@app_routers.post("/create-quiz", status_code=status.HTTP_201_CREATED)
def create_quiz(quiz: QuizCreator):
    return quizzes_collection.insert_one(jsonable_encoder(quiz))


@app_routers.get("/{id}")
def get_quiz_by_id(id: str):
    return all_quizzes(quizzes_collection.find({"_id": ObjectId(id)}))


@app_routers.delete("/{id}")
def delete_quiz(id: str):
    quizzes_collection.find_one_and_delete({"_id": ObjectId(id)})


@app_routers.put("/{id}")
def update_quiz_by_id(id: str, quiz: QuizCreator):
    quizzes_collection.find_one_and_update({"_id": ObjectId(id)}, {
        "$set": jsonable_encoder(quiz)
    })
    return all_quizzes(quizzes_collection.find({"_id": ObjectId(id)}))
