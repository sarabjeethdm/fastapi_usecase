# app/models/order_model.py

from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class OrderItem(BaseModel):
    product_id: str
    quantity: int = Field(gt=0)


class OrderCreate(BaseModel):
    user_id: str
    items: List[OrderItem]


class OrderInDB(BaseModel):
    id: str
    user_id: str
    items: List[OrderItem]
    total_price: float
    status: str
    created_at: datetime


class OrderResponse(OrderInDB):
    pass
