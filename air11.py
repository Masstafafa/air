
import sys

# Fonctions utilisées:

def get_pyramid(first_argument, second_argument):
    for i in range(second_argument):
      


# Gestion d'erreurs :

def is_valid_length(arguments: list[str]) -> bool: 
    if len(arguments) != 2:
        print("Erreur : Merci d'indiquer deux arguments qui seront des nombres entiers")
        return False
    return True

def is_alpha(first_argument: str) -> bool:
    if not first_argument.isalpha():
        print("Erreur : Merci d'indiquer un caractere")
        return False
    return True

def is_digit(second_argument: str) -> bool:
    if not second_argument.isdigit():
        print("Erreur : Merci d'indiquer uniquement des nombres entiers")
        return False
    return True

# Récupération de données :
def get_arguments() -> list[str]:
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def display_pyramid() -> None:
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    
    first_argument = arguments[0]
    if not is_alpha(first_argument):
        return
    
    second_argument = arguments[1]
    if not is_digit(second_argument):
        return
    
    pyramid = get_pyramid(first_argument, second_argument)
    

# Affichage :

display_pyramid()