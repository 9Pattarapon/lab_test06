from fastapi import APIRouter
from models.years_model import Years
import datetime

y = datetime.datetime.now()
years_api_router = APIRouter()

@years_api_router.get("/service/getage")
async def get_test(year:int):

    if year <= 0 :
        return {"age": "years not less than 0"}
    elif year > (y.year + 543) :
        return {"age": "unable to calculate"}
    else:
        age = (y.year + 543) - year
        return {"age": age}

        