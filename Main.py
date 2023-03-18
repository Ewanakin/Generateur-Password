from PasswordGenerator import PasswordGenerator
from BddPassword import BddPassword
import json

# fonction pour saisir les informations de connexion
def connexionBdd():
    with open("config.json") as file:
        data = json.load(file)
        host = data["host"]
        username = data["username"]
        password = data["password"]
        database = data["database"]
        connexionDb = BddPassword(host, username, password, database)
        if connexionDb.CreateConnexion():
            return connexionDb
        else:
            return False

def view_applications(connexionDB):
    allApplications = []
    listPassword = connexionDB.selectPassword()
    for element in listPassword:
        appPassword = PasswordGenerator(element[1], element[2], password=element[3])
        allApplications.append(appPassword)
    for application in allApplications:
        print("L'application : ", application.application, " avec le nom d'utilisateur : ", application.username, "\n"
              "possède le mot de passe : ", application.password)

    # connexionDB.viewPassword()
    # print("L'application : ", object.get_application(), " avec le nom d'utilisateur : ", object.get_username(), "\n"
    #       "possède le mot de passe : ", object.get_password())

connexionDB = connexionBdd()
if connexionDB != False:
    view_applications(connexionDB)
    createPassword = input("Souhaitez vous créer un mot de passe pour une application y/yes ? : ")
    while createPassword == "y" or createPassword == "yes":
        application = input("Saisir le nom de l'application : ")
        username = input("Saisir le nom d'utilisateur : ")
        #default variable
        verifLenPassword = False
        lenPassword=12
        # boucle vérification de la saisie de la longueur du mot de passe
        while not verifLenPassword:
            try:
                lenPassword = int(input("choisir une taille du mot de passe supérieur à 12 et inférieur à 30 : "))
                if 12 <= lenPassword <= 30:
                    verifLenPassword = True
                else:
                    print("La valeur doit être supérieur ou égale à 12")
            except:
                print("Merci de renter un entier ou de ne pas laisser le champ vide")

        appPassword = PasswordGenerator(application, username, lenPassword)
        appPassword.generator()
        connexionDB.insertPassword(appPassword.application, appPassword.username, appPassword.password)

        createPassword = input("Souhaitez vous à nouveau créer un mot de passe y/yes ? :")

