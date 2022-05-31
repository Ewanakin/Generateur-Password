from PasswordGenerator import PasswordGenerator
def verif_empty(saisieUti):
    if saisieUti == "":
        return True

def verif_char(saisieUti):
    for caractere in range(len(saisieUti)):
        for banCharacter in range(len(listCara)):
            if saisieUti[caractere] == listCara[banCharacter]:
                return True


listCara = ["/", "@", ",", ".", "<", ">", "!", "§", ":", "?", ";", "*", "^", "{", "}", "=", "[", "]", "(", ")", "|", "`"]
objectPassword = []
# saisie des valeurs par un utilisateur et création d'un objet appPassword qui contient le mot de passe générer et le nom de l'app
createPassword = input("Souhaitez vous créer un mot de passe pour une application y/yes ? : ")
while createPassword == "y" or createPassword == "yes":
    verifLenPassword = True
    appName = input("test : ")
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

    while verifLenPassword:
        try:
            lenPassword = int(input("choisir une taille du mot de passe supérieur à 12 : "))
            if lenPassword >= 12:
                verifLenPassword = False
            else:
                print("La valeur doit être supérieur ou égale à 12")
        except:
            print("Merci de renter un entier ou de ne pas laisser le champ vide")

    appPassword = PasswordGenerator(appName, lenPassword)
    appPassword.generator()
    objectPassword.append(appPassword)

    createPassword = input("Souhaitez vous à nouveau créer un mot de passe y/yes ? :")

for app in objectPassword:
    print(app.get_appName())
    print(app.get_password())
