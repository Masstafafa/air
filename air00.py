import sys

# Fonctions utilisées:
def get_values(arguments):
    arguments.sort()
    number_min = int(arguments[0])
    number_max = int(arguments[1])
    
    for i in range(number_min, number_max):
        print(i, end=" ")


# Gestion d'erreurs :
def is_valid_length(arguments):
    if len(arguments) != 1:
        print("Erreur : Merci d'indiquer un seul argument entre guillemets")
        return False
    return True

# Récupération de données :
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :
def display_numbers():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    if not is_valid_arguments(arguments):
        return
    get_values(arguments)
    
# Affichage :
display_numbers()