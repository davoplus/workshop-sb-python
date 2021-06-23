import mysql.connector

def mysqlConnection(dbJsonData):
    
    ENDPOINT=dbJsonData['host']
    PORT=dbJsonData['port']
    USR=dbJsonData['username']
    DBNAME=dbJsonData['dbname']
    PASSWD =dbJsonData['password']
    
    
    try:
        conn =  mysql.connector.connect(host=ENDPOINT, user=USR, passwd=PASSWD, port=PORT, database=DBNAME)
        cur = conn.cursor()
        cur.execute("""SELECT * FROM Employee""")
        myresult = cur.fetchall()

        for x in myresult:
          print(x)
        
    except Exception as e:
        print("Database connection failed due to {0}".format(e))  
    finally:
      if conn.is_connected():
        conn.close()
        cur.close()
        print("MySQL connection is closed")
    
