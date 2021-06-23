import sys
import dbconnect
import threading
import datetime
import secrets
import json

secret_name = sys.argv[1]
region_name = "us-west-2"

dbInfoString = secrets.get_secret(secret_name, region_name)
print ( dbInfoString )
dbJsonData = json.loads(dbInfoString)

dbconnect.mysqlConnection(dbJsonData)
