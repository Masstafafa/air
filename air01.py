import sys

# Fonctions utilisées:
def split_chain(string_to_cut, string_separator):
    list = []
    while string_separator in string_to_cut:
        index_separator = string_to_cut.find(string_separator)
        length_separator = len(string_separator)
        list.append(string_to_cut[:index_separator])
        string_to_cut = string_to_cut[(index_separator + length_separator):]
    list.append(string_to_cut) 
    return list

# Gestion d'erreurs :
def is_valid_length(arguments):
    if len(arguments) != 2:
        print("Erreur : Merci d'indiquer deux arguments entre guillemets")
        return False
    return True

# Récupération de données :
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :
def get_split_chain():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    string_separator = arguments[1]
    return split_chain(arguments[0], string_separator)

# Affichage :
def display():
    splited_chain = get_split_chain()
    for word in splited_chain:
        print(word)

display()

