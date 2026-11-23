
"""Notification microservice - entry point.

Run: uvicorn app.main:app --reload --port 8084
  or: python -m app.main
"""

import os
from contextlib import asynccontextmanager

from fastapi import FastAPI
import py_eureka_client.eureka_client as eureka_client

from app.routers import notification

PORT = int(os.getenv("PORT", "8084"))

EUREKA_USERNAME = os.getenv("EUREKA_USERNAME", "admin")
EUREKA_PASSWORD = os.getenv("EUREKA_PASSWORD", "123456")


@asynccontextmanager
async def lifespan(app: FastAPI):

    # Register Notification in Eureka at startup
    print("Registering NOTIFICATION in Eureka...")

    await eureka_client.init_async(
        eureka_server="http://localhost:8761/eureka",
        app_name="NOTIFICATION",
        instance_port=PORT,
        instance_host="localhost",
        instance_ip="127.0.0.1",
        status_page_url="http://localhost:8084/health",
        health_check_url="http://localhost:8084/health",
        eureka_basic_auth_user=EUREKA_USERNAME,
        eureka_basic_auth_password=EUREKA_PASSWORD
    )

    print(f"NOTIFICATION registered on port {PORT}")

    yield

    # Unregister Notification from Eureka at shutdown
    print("Stopping NOTIFICATION...")

    await eureka_client.stop_async()

    print("NOTIFICATION stopped successfully")



app = FastAPI(
    title="Notification Microservice API",
    version="1.0.0",
    description=(
        "Notification microservice (Python / FastAPI, no database). "
        "Only the hello endpoint is implemented; the notification logic is to be developed by students."
    ),
    contact={"name": "Badia Abouhdid"},
    servers=[{"url": f"http://localhost:{PORT}", "description": "Local"}],
    docs_url="/swagger-ui",
    openapi_url="/v3/api-docs",
    redoc_url="/redoc",
    lifespan=lifespan
)
@app.get("/health")
async def health():
    return {
        "status": "UP",
        "service": "NOTIFICATION"
    }


app.include_router(notification.router)

# TODO (students): if you add other routers, include them here.


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=PORT,
        reload=True
    )
