import sys

# Fonctions utilisées:
def split_chain(string_to_cut, string_separator):
    temporary_word = ""
    list = []
    for chr in string_to_cut:
        if chr in string_separator:
            list.append(temporary_word)
            temporary_word = ""
        else : 
            temporary_word += chr
    if temporary_word != "":
        list.append(temporary_word)
    return list

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
def get_split_chain():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    string_separator = " ", "\n", "\t"
    return split_chain(arguments[0], string_separator)

# Affichage :
def display():
    splited_chain = get_split_chain()
    for word in splited_chain:
        print(word)

display()
