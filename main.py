from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get('/')
def read_root():
    return {'Hello': 'World'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = '42'):
    return {'item_id': item_id, 'q': q}


@app.put('/items/{item_id}')
def update_item(item_id: int, item: Item):
    if item.is_offer:
        answer = 'Sure'
    else:
        answer = 'Out of Stock'
    return {
        'item_id': item_id,
        'item_name': item.name,
        'item_price': item.price,
        'is on sale': answer
    } 

