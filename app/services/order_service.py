# app/services/order_service.py

from datetime import datetime
from typing import List

from app.db.base import (
    create_document,
    get_document,
    get_all_documents,
)
from app.models.order_model import OrderCreate, OrderResponse


COLLECTION = "orders"

# Mock price catalog
PRODUCT_PRICES = {
    "p1": 100.0,
    "p2": 250.0,
    "p3": 500.0,
}


class OrderService:

    @staticmethod
    async def create_order(order_data: OrderCreate) -> OrderResponse:
        total = 0.0

        for item in order_data.items:
            if item.product_id not in PRODUCT_PRICES:
                raise ValueError(f"Invalid product_id: {item.product_id}")
            total += PRODUCT_PRICES[item.product_id] * item.quantity

        document = {
            "user_id": order_data.user_id,
            "items": [item.dict() for item in order_data.items],
            "total_price": total,
            "status": "pending",
            "created_at": datetime.utcnow(),
        }

        inserted_id = await create_document(COLLECTION, document)

        document["id"] = inserted_id
        return OrderResponse(**document)

    @staticmethod
    async def get_order(order_id: str) -> OrderResponse:
        doc = await get_document(COLLECTION, order_id)
        if not doc:
            raise ValueError("Order not found")

        doc["id"] = doc.pop("_id")
        return OrderResponse(**doc)

    @staticmethod
    async def get_all_orders() -> List[OrderResponse]:
        docs = await get_all_documents(COLLECTION)
        orders = []

        for doc in docs:
            doc["id"] = doc.pop("_id")
            orders.append(OrderResponse(**doc))

        return orders

