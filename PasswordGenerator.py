from random import choice
class PasswordGenerator:

    def __init__(self,appName,lenPassword):
        self.appName = appName
        self.lenPassword = lenPassword
        self.password = ""
        self.caracList = ["a","b"]
        self.caracPasswordList = []

    def get_appName(self):
        return self.appName
    def get_lenPassword(self):
        return self.lenPassword
    def get_password(self):
        return self.password

    def generator(self):
        for nbCarac in range(self.lenPassword):
            self.caracPasswordList.append(choice(self.caracList))
        self.password = "".join(self.caracPasswordList)


