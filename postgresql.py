import sys
import psycopg2
import secrets
import json

def postgresqlConnection(dbJsonData):
    
    ENDPOINT=dbJsonData['host']
    PORT=dbJsonData['port']
    USR=dbJsonData['username']
    DBNAME=dbJsonData['dbname']
    PASSWD =dbJsonData['password']
    
    
    try:
        conn =  psycopg2.connect(user=USR, password=PASSWD,host=ENDPOINT, port=PORT, database=DBNAME)
        cur = conn.cursor()
        cur.execute("""SELECT * FROM Employee""")
        myresult = cur.fetchall()

        for x in myresult:
          print(x)
        
    except Exception as e:
        print("Database connection failed due to {0}".format(e))  
    finally:
      if conn is not None:
        conn.close()
        cur.close()
        print("Postgress connection is closed")

secret_name = sys.argv[1]
region_name = "us-west-2"

dbInfoString = secrets.get_secret(secret_name, region_name)
print ( dbInfoString )
dbJsonData = json.loads(dbInfoString)
postgresqlConnection(dbJsonData)
