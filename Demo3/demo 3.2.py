import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import gspread
import json
import sys
import datetime

from oauth2client.service_account import ServiceAccountCredentials

sensor = Adafruit_DHT.DHT11

SENS=4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENS, GPIO.IN)

humidity, temperature = Adafruit_DHT.read_retry(sensor, SENS)

GDOCS_OAUTH_JSON       = 'CollianderJeremias345-9a89cbd7ec3b.json'

GDOCS_SPREADSHEET_NAME = 'IoT 345'

FREQUENCY_SECONDS      = 1

def login_open_sheet(oauth_key_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    try:
        scope =  ['https://spreadsheets.google.com/feeds']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1
        return worksheet
    except Exception as ex:
        print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)
		
worksheet = None
while True:
    # Login if necessary.
    if worksheet is None:
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

    humidity, temp = Adafruit_DHT.read(sensor, SENS)

    
    if humidity is None or temp is None:
        time.sleep(2)
        continue

    print('Temperature: {0:0.1f} C'.format(temp))
    print('Humidity:    {0:0.1f} %'.format(humidity))

    try:
        worksheet.append_row((datetime.datetime.now(), temp, humidity))
    except:
       
        print('Append error, logging in again')
        worksheet = None
        time.sleep(FREQUENCY_SECONDS)
        continue

    # Wait 30 seconds before continuing
    print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
    time.sleep(FREQUENCY_SECONDS)

GPIO.cleanup()