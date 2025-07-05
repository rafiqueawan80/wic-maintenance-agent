import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime
print("✅ Row started")
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service-account.json", scope)
client = gspread.authorize(creds)

sheet = client.open("WIC_Maintenance_Requests").worksheet("Sheet1")  # <-- adjust name if needed

timestamp = str(datetime.now())
row = [999, timestamp, "Debug Test", "Still testing...", "low", "new"]
sheet.append_row(row)

print("✅ Row added")
