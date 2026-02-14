# app/api/order_route.py

from typing import List

from fastapi import APIRouter, HTTPException

from app.models.order_model import OrderCreate, OrderResponse
from app.services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderResponse)
async def create_order(order: OrderCreate):
    try:
        return await OrderService.create_order(order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{order_id}", response_model=OrderResponse)
async def get_order(order_id: str):
    try:
        return await OrderService.get_order(order_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=List[OrderResponse])
async def get_all_orders():
    return await OrderService.get_all_orders()
