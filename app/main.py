from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.database import engine, Base
from app.api import orders, products

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=settings.app_name,
    description="Order Processing API — built for Rakuten interview preparation",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(orders.router,   prefix=settings.api_v1_prefix)
app.include_router(products.router, prefix=settings.api_v1_prefix)


@app.get("/api/v1/health", tags=["Health"])
def health_check():
    """Health check endpoint — used by load balancers / Kubernetes liveness probe."""
    return {
        "status": "healthy",
        "service": settings.app_name,
        "env": settings.env,
    }
