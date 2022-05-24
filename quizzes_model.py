from pydantic import BaseModel


class Quiz(BaseModel):
    question: str
    choices: list = []


class QuizCreator(BaseModel):
    name: str
    quiz_list: list[Quiz, None] = None


def quiz_form(quiz: QuizCreator):
    return {
        "id": str(quiz["_id"]),
        "name": quiz["name"],
        "quiz_list": quiz["quiz_list"]
    }


def all_quizzes(quizzes_):
    return [quiz_form(quiz) for quiz in quizzes_]
