import sys

# Fonctions utilisées:

def split_string(string_to_cut: str, separator: str) -> list[str]:
    split_words = []
    separators_counter = string_to_cut.count(separator)
   
    for i in range(separators_counter):
       index_separator = string_to_cut.find(separator)
       length_separator = len(separator)
       split_words.append(string_to_cut[:index_separator])
       string_to_cut = string_to_cut[(index_separator + length_separator):]
    split_words.append(string_to_cut)
    return split_words

# Gestion d'erreurs :

def is_valid_length(arguments: list[str]) -> bool:
    if len(arguments) != 2:
        print("Erreur : Merci d'indiquer deux arguments entre guillemets")
        return False
    return True

# Récupération de données :

def get_arguments() -> list[str]:
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def print_splited_string() -> list[str] | None:
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    
    separator = arguments[1]
    string_to_cut = arguments[0]
    splited_chain = split_string(string_to_cut, separator)
    for word in splited_chain:
        print(word)

# Affichage :

print_splited_string()

