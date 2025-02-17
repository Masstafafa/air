import sys

# Fonctions utilisées:

def assemble_chains(list_of_words: list[str], separator: str) -> str:
    final_string = ''
    for string in list_of_words[:-1]: #check tous les arguments sauf le dernier qui est le separateur
        final_string += string #ajoute le mot
        final_string += separator #ajoute le separateur
    final_string += list_of_words[-1]  # ajoute le dernier mot sans séparateur
    return final_string

# Gestion d'erreurs :

def is_valid_length(arguments: list[str]) -> bool:
    if len(arguments) < 3:
        print("Erreur : Merci d'indiquer un minimum de trois arguments entre guillemets, deux arguments et un séparateur")
        return False
    return True

# Récupération de données :

def get_arguments() -> list[str]:
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def display_assembled_chains() -> list[str] | None:
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    list_of_words = arguments[:-1]
    separator = arguments[-1]
    assembled_chains = assemble_chains(list_of_words, separator)
    print(assembled_chains)

# Affichage :

display_assembled_chains()

