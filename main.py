from fastapi import FastAPI
from routes.years_route import years_api_router

app = FastAPI()

app.include_router(years_api_router)
