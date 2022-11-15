from faker import Faker
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
name = ""



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
    print(name)
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
