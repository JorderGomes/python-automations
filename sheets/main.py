import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1zCHSotE1pPC9jnu4yiroT6XVpCYvP2bzO_RJpLXx14Q"
SAMPLE_RANGE_NAME = "Página1!A1:D15"

def cipher_to_number(cipher):
    cipher = cipher.replace("R$ ","").replace(".","")
    cipher = cipher.replace(",",".")
    number = float(cipher)
    return number

def main():
    creds = None
    if os.path.exists(".ignored-files/token.json"):
        creds = Credentials.from_authorized_user_file(
            ".ignored-files/token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                ".ignored-files/credentials_sheets.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        with open(".ignored-files/token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )

        values = result['values']
        new_values = [
            ["Valor líquido"]
        ]
        for i, line in enumerate(values):
            if i > 0:
                liquid = cipher_to_number(line[1]) - cipher_to_number(line[2])
                new_values.append([liquid])

        # new_values = [
        #     ["Fevereiro","R$ 48.233,00"]
        # ]
        result = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, 
                range="D1", 
                valueInputOption="USER_ENTERED", 
                body={'values':new_values}).execute()

    except HttpError as err:
        print(err)


if __name__ == "__main__":
    main()
