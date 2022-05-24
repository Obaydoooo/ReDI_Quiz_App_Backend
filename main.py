from fastapi import FastAPI
from quizzes_routes import app_routers

app = FastAPI(title="Quiz_APP")

app.include_router(app_routers)


