from fastapi import FastAPI
from app.controllers.user_controller import router as user_router
from app.controllers.task_controller import router as task_router

app = FastAPI()

app.include_router(user_router)
app.include_router(task_router)

