import sys

# Fonctions utilisées:

def split_string(string_to_cut: str, string_separator: list[str]) -> list[str]:
    current_word: str = ""
    new_list: list[str] = []
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

def is_valid_length(string: list[str]) -> bool:
    if len(string) != 1:
        print("Erreur : Merci d'indiquer un seul argument entre guillemets")
        return False
    return True

# Récupération de données :

def get_arguments() -> list[str]:
    arguments: list[str] = sys.argv[1:]
    return arguments

# Résolution :

def display_splited_chain() -> None:
    string: list[str] = get_arguments()
    if not is_valid_length(string):
        return
    
    string_separator: list[str] = [" ", "\n", "\t"]
    string_to_cut: str = string[0]
    splited_chain: list[str] = split_string(string_to_cut, string_separator)
    for word in splited_chain:
        print(word)

# Affichage :

display_splited_chain()
