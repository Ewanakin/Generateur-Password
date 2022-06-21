import mysql.connector
class BddPassword:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.mydb = ""


    """# définir la nouvelle valeur de la database pour la connexion a la db
    def set_database(self, database):
        self.database = database"""

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

    """    # methode de connexion à une base de donnée
    def ConnectToDb(self, database):
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=database,
            )
            return True
        except:
            return False
    """
    def insertPassword(self, appName, password):
        cursor = self.mydb.cursor()
        req = ("INSERT INTO password(appName, password) VALUES(%s,%s)")
        data = (appName, password)

        cursor.execute(req, data)

        self.mydb.commit()

        cursor.close()