import csv
import gspread
import json
import pprint
from oauth2client.service_account import ServiceAccountCredentials 
from dotenv import load_dotenv
import os
load_dotenv()

SPREADSHEET_ID = os.getenv('SPREADSHEET_ID')

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('credential.json', scope)

gc = gspread.authorize(credentials)

SPREADSHEET_KEY = SPREADSHEET_ID

worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

with open("selif.csv", 'w') as f:
    writer= csv.writer(f)
    pprint.pprint(worksheet.get_all_values())
    writer.writerows(worksheet.get_all_values())