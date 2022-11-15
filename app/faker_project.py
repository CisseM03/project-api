from faker import Faker
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost/",
    "http://localhost:8080/",
    "https://localhost.tiangolo.com/",
    "http://127.0.0.1:5500/",
    "https://CisseM03.github.io/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

name = "identify yourself!"

class Person(BaseModel):
    first_name: str
    last_name: str


@app.post("/cards")
async def create_item(item: Person):
    global name
    name = item.__getattribute__("first_name") + " " + item.__getattribute__("last_name")
    return name


@app.get("/user")
async def yourname():
    return "Your name is:", name


@app.get("/japan")
async def japname():
    fake = Faker('ja_JP')
    named = fake.name()
    return {"message": "Your japanese name would be:", "name": named}


@app.get("/american")
async def americanname():
    fake = Faker('en_US')
    named = fake.name()
    return {"message": "Your american name would be:", "name": named}

# uvicorn faker_project:app --reload
