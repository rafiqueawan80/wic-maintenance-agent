import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime

# CONFIGURE THESE
SHEET_NAME = "WIC_Maintenance_Requests"
CREDENTIALS_FILE = "service-account.json"  # path to your downloaded JSON

# AUTH
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
creds = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, scope)
client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME).worksheet("Sheet1")

# CREATE NEW REQUEST
def create_request(location, issue, priority="medium"):
    print("📡 Connecting to sheet...")
    next_id = len(sheet.get_all_values())  # Row count = ID
    print(f"Current row count: {len(sheet.get_all_values())}")
    timestamp = str(datetime.now())
    sheet.append_row([next_id, timestamp, location, issue, priority, "new"])
    return {"id": next_id, "status": "new", "location": location, "issue": issue}

# GET ALL REQUESTS
def get_all_requests():
    return sheet.get_all_records()

# UPDATE STATUS
def update_request_status(request_id, new_status):
    cell = sheet.find(str(request_id))
    sheet.update_cell(cell.row, 6, new_status)
    return f"Updated request {request_id} to status: {new_status}"
