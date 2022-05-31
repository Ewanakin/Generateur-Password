import mysql.connector
class BddPassword:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password
        self.database = ""
        self.mydb = ""
        self.mycursor = ""

    # définir la nouvelle valeur de la database pour la connexion a la db
    def set_database(self, database):
        self.database = database

    # initialisation de la connexion
    def CreateConnexion(self):
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
            )
            return True
        except:
            return False

    # methode de connexion à une base de donnée
    def ConnectToDb(self):
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