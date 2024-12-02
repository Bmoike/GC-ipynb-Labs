from fastapi import FastAPI
from pydantic import BaseModel
import random

# create a fast api instance
app = FastAPI()



# facts class
class randomFacts(BaseModel):
    id: int
    fact: str

# list of facts
FactDB = [randomFacts(id=0, fact='Penguins mate for life.'), randomFacts(id=1, fact='Canadian Northwest Territories License plates are shaped like polar bears.'),
         randomFacts(id=2, fact='The Governor of Moscow trained a large bear to serve pepper Vodka to his guests.')]



# returns the whole data base
@app.get('/')
async def get_all():
    return FactDB

@app.get('/fact')
async def random_fact():
    return random.choice(FactDB)

# returns an object based on an id input
@app.get('/fact/{id}')
async def get_id(id):
    
    return (i for i in FactDB if i.id == int(id))


# adds new facts and returns the fact so user knows it was added to FactDB
@app.post('/')
async def add(NewFact: randomFacts):
    FactDB.append(NewFact)
    return NewFact

