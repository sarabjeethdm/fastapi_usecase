# app/main.py

from fastapi import FastAPI
from slowapi.errors import RateLimitExceeded
from slowapi.middleware import SlowAPIMiddleware

from app.api.auth_route import router as auth_router
from app.api.health_route import router as health_router
from app.api.order_route import router as order_router
from app.api.user_route import router as user_router
from app.core.rate_limiter import limiter, rate_limit_exceeded_handler

app = FastAPI()

# Attach limiter to app
app.state.limiter = limiter

# Add middleware
app.add_middleware(SlowAPIMiddleware)

# Add exception handler
app.add_exception_handler(RateLimitExceeded, rate_limit_exceeded_handler)

app.include_router(user_router)
app.include_router(auth_router)
app.include_router(health_router)
app.include_router(order_router)
