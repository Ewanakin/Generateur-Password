import mysql.connector
class BddPassword:
    def __init__(self, host, user, password):
        self.host = host
        self.user = user
        self.password = password

    def DbConnexion(self):
        try:
            return mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password
            )
        except:
            return True