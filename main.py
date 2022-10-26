from email.headerregistry import Address
from fastapi import FastAPI
from pydantic import BaseModel

# initiate the app
app = FastAPI(
    title="Address_Book",
    description="Automatic Documentation",
    
)

# In memory DB
db: dict = {}



# modelAddress_Book
class Address_Book(BaseModel):
    City: str
    Latitude: float
    Longitude: float


@app.get('/retrive')
def get_record():
    return db


@app.post('/create')
def post_rec(sl_no: int, City: str, Longitude: float,Latitude:float):
    rec = {
        "City": City,
        "Latitude": Latitude,
        "Longitude": Longitude,        
    }

    db[sl_no] = rec
    return rec


@app.post('/insert')
def insert_rec(sl_no: int, Address_Book: Address_Book):
    rec = {
        "City": Address_Book.City,
        "Latitude": Address_Book.Latitude,
        "Longitude": Address_Book.Longitude
    }

    db[sl_no] = rec
    return rec


@app.put('/update')
def update_rec():
    db.query(Address_Book).filter(Address_Book.City).update(vars(Address))
    db.commit()
    return db.query(Address_Book).filter(Address_Book.City).first()

@app.delete('/delete')
def delete_rec():
    pass
