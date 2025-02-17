import sys

# Fonctions utilisées:
def split_string(string_to_cut, string_separator):
    current_word = ""
    new_list = []
    for char in string_to_cut:
        if char in string_separator:
            new_list.append(current_word)
            current_word = ""
        else : 
            current_word += char
    if  current_word != "":
        new_list.append(current_word)
    return new_list

# Gestion d'erreurs :
def is_valid_length(string):
    if len(string) != 1:
        print("Erreur : Merci d'indiquer un seul argument entre guillemets")
        return False
    return True

# Récupération de données :
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :
def display_splited_chain():
    string = get_arguments()
    if not is_valid_length(string):
        return
    
    string_separator = " ", "\n", "\t"
    string_to_cut = string[0]
    splited_chain = split_string(string_to_cut, string_separator)
    for word in splited_chain:
        print(word)

# Affichage :

display_splited_chain()
