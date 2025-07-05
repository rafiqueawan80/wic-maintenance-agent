from google_sheets_backend import create_request, get_all_requests, update_request_status

# Create a test maintenance request
result = create_request(
    location="Main Hall",
    issue="Broken ceiling tile",
    priority="high"
)
print("✅ Created:", result)

# Get all maintenance requests
all_requests = get_all_requests()
print("📋 All Requests:")
for req in all_requests:
    print(req)

# Update the status of the request (optional)
updated = update_request_status(result["id"], "in progress")
print("🔁 Status Update:", updated)
