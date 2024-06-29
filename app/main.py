from fastapi import FastAPI
from pydantic import BaseModel
import json
from .agent import BookAgent

app = FastAPI()

# Load book data
with open('data/books.json') as f:
    books_data = json.load(f)

# Initialize the agent
agent = BookAgent(books_data)

class GenreRequest(BaseModel):
    genre: str

@app.post("/top_books")
async def top_books(request: GenreRequest):
    top_books = agent.get_top_books(request.genre)
    return {"top_books": top_books}

@app.post("/top_10_books")
async def top_10_books(request: GenreRequest):
    top_10_books = agent.get_top_10_books(request.genre)
    return {"top_10_books": top_10_books}

@app.post("/user_book")
async def user_book(request: GenreRequest):
    user_book = agent.get_book_for_user(request.genre)
    return {"user_book": user_book}

@app.get("/conclude")
async def conclude():
    message = agent.conclude_task()
    return {"message": message}
