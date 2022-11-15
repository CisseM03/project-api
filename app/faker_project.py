from faker import Faker
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Person(BaseModel):
    first_name: str
    last_name: str

@app.post("/yourname")
async def create_item(item: Person):
   x = {"name": item.__getattribute__("first_name"),"last_name": item.__getattribute__("last_name")}

   with open("name.json", "w") as file:
    file.write(str(x))


@app.get("/japan")
async def japname():
    fake = Faker('ja_JP')
    named = fake.name()
    return {"message": "Your japanese name would be:", "name": named}


@app.get("/america")
async def americanname():
    fake = Faker('en_US')
    named = fake.name()
    return {"message": "Your american name would be:", "name": named}

# uvicorn faker_project:app --reload
