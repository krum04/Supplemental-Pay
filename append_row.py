import gspread

from google.oauth2.service_account import Credentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
scopes = ['https://www.googleapis.com/auth/spreadsheets',
          'https://www.googleapis.com/auth/drive']

credentials = Credentials.from_service_account_file('creds.json', scopes=scopes)

def append_row(period,lname,fname,empId,hours):
    gc = gspread.authorize(credentials)

    gauth = GoogleAuth()
    drive = GoogleDrive(gauth)

    # open a google sheet
    gs = gc.open_by_key('1pIMq4bSv0F09i_xztBQjzHGBzvaCER2-sQWAce462KA')
    # select a work sheet from its name
    worksheet1 = gs.worksheet(f'Period {period}')
    row = [lname,fname,empId]
    for hour in hours:
        row.append(hour)  

    print(worksheet1.append_row(row))

