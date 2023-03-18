from random import choice
class PasswordGenerator:

    def __init__(self, application, username, lenPassword=None, password=None,):
        self.application = application
        self.username = username
        self.lenPassword = lenPassword
        self.password = password
        self.caracList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","1","2","3","4","5","6","7","8","9","'","!","?",".","/","*","*","-","_","ç",",",";","#","$","~","|"]
        self.caracPasswordList = []

    def get_application(self):
        return self.application

    def get_password(self):
        return self.password

    def get_username(self):
        return self.username

    def generator(self):
        for nbCarac in range(self.lenPassword):
            self.caracPasswordList.append(choice(self.caracList))
        self.password = "".join(self.caracPasswordList)




