
HOST = '13.114.30.166'
PORT = 3309
USER_NAME = 'view'
PASS_WORD = 'View@1234%^&*'
DATABASE = "ecor"
import mysql.connector
class BaseData():
    def __init__(self):
        self.cnx = mysql.connector.connect(user = USER_NAME,password=PASS_WORD,host=HOST,port=PORT,database=DATABASE)
    def execute_query(self,query):
        cursor = self.cnx.cursor()
        cursor.execute(query)
        cursor.close()
        self.cnx.close()
