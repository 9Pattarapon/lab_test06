from fastapi import FastAPI
from routes.todos_route import todo_api_router
from routes.years_route import years_api_router

app = FastAPI()

app.include_router(todo_api_router)
app.include_router(years_api_router)

