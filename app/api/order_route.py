# app/api/order_route.py

from typing import List

from fastapi import APIRouter, HTTPException, Request

from app.core.rate_limiter import limiter
from app.models.order_model import OrderCreate, OrderResponse
from app.services.order_service import OrderService

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.post("/", response_model=OrderResponse)
@limiter.limit("5/minute")
async def create_order(request: Request, order: OrderCreate):
    try:
        return await OrderService.create_order(order)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{order_id}", response_model=OrderResponse)
@limiter.limit("20/minute")
async def get_order(request: Request, order_id: str):
    try:
        return await OrderService.get_order(order_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/", response_model=List[OrderResponse])
@limiter.limit("30/minute")
async def get_all_orders(request: Request):
    return await OrderService.get_all_orders()
