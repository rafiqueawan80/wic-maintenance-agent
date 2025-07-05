from fastapi import FastAPI
from pydantic import BaseModel
from google_sheets_backend import create_request, get_all_requests, update_request_status
from fastapi.openapi.utils import get_openapi


app = FastAPI()
# Inject your own openapi schema
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="WIC Maintenance Agent",
        version="1.0.0",
        description="API for creating and managing repair and maintenance requests.",
        routes=app.routes,
    )
    openapi_schema["servers"] = [
        {
            "url": "https://wic-maintenance-agent.onrender.com",
            "description": "Production server"
        }
    ]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

class RequestCreate(BaseModel):
    location: str
    issue: str
    priority: str = "medium"

class StatusUpdate(BaseModel):
    request_id: int
    new_status: str

@app.post("/create_request")
def api_create_request(data: RequestCreate):
    return create_request(data.location, data.issue, data.priority)

@app.get("/get_all_requests")
def api_get_all_requests():
    return get_all_requests()

@app.post("/update_request_status")
def api_update_status(data: StatusUpdate):
    return update_request_status(data.request_id, data.new_status)
app.openapi = custom_openapi