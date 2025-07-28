from pydantic import BaseModel

class MyDataOutput(BaseModel):
    name: str
    age: int
    email: str
    phone: str
    address: str
    city: str
    state: str
    zip: str
    country: str
    website: str