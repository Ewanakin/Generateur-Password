from PasswordGenerator import PasswordGenerator
from BddPassword import BddPassword

# vérification si la saisie n'est pas vide
def verif_empty(saisieUti):
    if saisieUti == "":
        return True

# vérification de la saisie utilisateur
def verif_char(saisieUti):
    for caractere in range(len(saisieUti)):
        for banCharacter in range(len(listCara)):
            if saisieUti[caractere] == listCara[banCharacter]:
                return True

# fonction pour saisir les informations de connexion
def connexionBdd():
    host = input("merci de saisir l'host de la base de donnée : ")
    user = input("merci de saisir le nom d'utilisateur de la base de donnée : ")
    password = input("merci de saisir le mot de passe de la base de donnée : ")
    database = input("merci de saisir le mot de passe de la base de donnée : ")
    connexionDb = BddPassword(host, user, password, database)
    # si connexion réussi alors renvoyer l'objet de connexion
    if connexionDb.CreateConnexion():
        print("Connexion réussie")
        return connexionDb
    else:
        return False

connBdd = connexionBdd()
while connBdd == False:
    print("Les informations sont incorrectes")
    connBdd = connexionBdd()


listCara = ["/", "@", ",", ".", "<", ">", "!", "§", ":", "?", ";", "*", "^", "{", "}", "=", "[", "]", "(", ")", "|", "`"]
objectPassword = []
# Création d'un mot de passe associé à un nom d'application
createPassword = input("Souhaitez vous créer un mot de passe pour une application y/yes ? : ")
while createPassword == "y" or createPassword == "yes":
    verifLenPassword = True
    appName = input("Saisir le nom de l'application : ")
    # boucle vérification de la saisie du nom de l'appli
    while verif_empty(appName) or verif_char(appName):
        if not verif_empty(appName):
            if verif_char(appName):
                errorCaract = "Merci de ne pas choisir un caractère de la liste "
                for i in range(len(listCara)):
                    errorCaract += listCara[i]
                print(errorCaract)
                appName = input("Merci de saisir un nom d'application valide : ")
        else:
            print("Il est nécessaire de remplir le nom de l'application")
            appName = input("Merci de saisir un nom d'application valide : ")
    # boucle vérification de la saisie de la longueur du mot de passe
    while verifLenPassword:
        try:
            lenPassword = int(input("choisir une taille du mot de passe supérieur à 12 et inférieur à 100 : "))
            if lenPassword >= 12 and lenPassword <= 100:
                verifLenPassword = False
            else:
                print("La valeur doit être supérieur ou égale à 12")
        except:
            print("Merci de renter un entier ou de ne pas laisser le champ vide")
    # Création de l'objet Password et ajout dans la liste des objets
    appPassword = PasswordGenerator(appName, lenPassword)
    appPassword.generator()
    objectPassword.append(appPassword)

    createPassword = input("Souhaitez vous à nouveau créer un mot de passe y/yes ? :")


for passwordApp in objectPassword:
    print(passwordApp.get_appName())
    print(passwordApp.get_password())
    connBdd.insertPassword(passwordApp.get_appName(), passwordApp.get_password())
