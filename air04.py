import sys

# Fonctions utilisées:

def remove_consecutive_character(string: str) -> str:
    new_string = '' #Création d'une variable pour mettre la phrase
    for i in range(len(string) -1): #longueur de la phrase
        current_chr = string[i]
        next_chr = string[i + 1]
        if current_chr != next_chr:
            new_string += current_chr
    new_string += string[-1] #dernière lettre
    return new_string

# Gestion d'erreurs :

def is_valid_length(arguments: list[str]) -> bool:
    if len(arguments) != 1:
        print("Erreur : Merci d'indiquer une seule phrase entre guillemets")
        return False
    return True

# Récupération de données :

def get_arguments() -> list[str]:
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def display_no_consecutive_character() -> None:
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    
    string = arguments[0]
    final_string = remove_consecutive_character(string)
    print(final_string)

# Affichage :

display_no_consecutive_character()
