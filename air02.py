import sys

# Fonctions utilisées:
def assemble_chain(array_of_strings, separator):
    final_string = ''
    for string in array_of_strings[:-1]: #check tous les arguments sauf le dernier qui est le separateur
        final_string += string #ajoute le mot
        final_string += separator #ajoute le separateur
    final_string += array_of_strings[-2]  # ajoute le dernier mot sans séparateur
    return final_string

# Gestion d'erreurs :
def is_valid_length(arguments):
    if len(arguments) < 3:
        print("Erreur : Merci d'indiquer un minimum de trois arguments entre guillemets, deux arguments et un séparateur")
        return False
    return True

# Récupération de données :
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :
def get_assembled_chain():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    separator = arguments[-1]
    return assemble_chain(arguments[:-1], separator)

# Affichage :
def display():
    assembled_chain = get_assembled_chain()
    if assembled_chain is not None:  # Vérifie si on a un résultat
        print(assembled_chain)

display()
