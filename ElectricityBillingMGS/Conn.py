import mysql.connector


class Conn:
    def __init__(self):
        pass

    def makeConnection(self):
        # Connect to the Mysql database
        try:

            db_conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="xxxxxxxxxxxxx",
            database="ebsys"

             )

        # check connection is successful
            if db_conn.is_connected():
               print("Connection Successful")

               return db_conn


            else:
               print("Connection failed")

        except mysql.connector.Error as e:
            print(str(e))

        except Exception as e:
            print(str(e))






