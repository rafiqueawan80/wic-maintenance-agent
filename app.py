from fastapi import FastAPI
from pydantic import BaseModel
from google_sheets_backend import create_request, get_all_requests, update_request_status

app = FastAPI()

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
