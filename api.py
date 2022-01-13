from fastapi import FastAPI, HTTPException
from main import recommendations
from datasets import DATASET_FULL

app = FastAPI()


@app.get("/")
async def read_index():
    return {"message": "Welcome!"}


@app.get("/recommend")
async def get_recommendation(title: str):
    recom = recommendations(title)
    if not recom:
        raise HTTPException(status_code=404, detail="Requested title not found!")

    return {"data": recom, "status": 200}


@app.get("/titles")
async def read_all_movies():
    movies = list(DATASET_FULL["title"])
    return {"status": 200, "data": movies}, 200
