import mysql.connector
class BddPassword:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.mydb = ""

    # initialisation de la connexion
    def CreateConnexion(self):
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
            )
            return True
        except:
            return False

    def insertPassword(self, application, username, password):
        cursor = self.mydb.cursor()
        req = ("INSERT INTO password(application, username, password) VALUES(%s,%s,%s)")
        data = (application, username, password)
        cursor.execute(req, data)
        self.mydb.commit()
        cursor.close()

    def selectPassword(self):
        cursor = self.mydb.cursor()
        cursor.execute("SELECT * FROM password")
        passwordList = cursor.fetchall()
        cursor.close()
        return passwordList