
import sys

# Fonctions utilisées:

def get_pyramid(char_for_pyramid, number_of_floor):
    floors = int(number_of_floor)
    pyramid = []
    for i in range(floors):
        spaces = (floors - 1) - i
        chars = 1 + (2 * i)
        line = (" " * spaces) + (char_for_pyramid * chars)
        pyramid.append(line)  
    return "\n".join(pyramid)


# Gestion d'erreurs :

def is_valid_length(arguments: list[str]) -> bool: 
    if len(arguments) != 2:
        print("Erreur : Merci d'indiquer deux arguments : un caractere et nombre entier")
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
    
    char_for_pyramid = arguments[0]
    if not is_alpha(char_for_pyramid):
        return
    
    number_of_floor = arguments[1]
    if not is_digit(number_of_floor):
        return
    
    pyramid = get_pyramid(char_for_pyramid, number_of_floor)
    print(pyramid)

# Affichage :

display_pyramid()