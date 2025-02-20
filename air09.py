
import sys

# Fonctions utilisées:
def rotate_position_on_left(input_list: list[str]) -> list[str]:
    debut_list = input_list[1:]
    end_list = [input_list[0]]
    rotated_list = debut_list + end_list
    return rotated_list

# Gestion d'erreurs :

def is_valid_length(arguments: list[str]) -> bool: #vérifie qu'il y a bien deux argumens au moins
    if len(arguments) < 2:
        print("Erreur : Merci d'indiquer au moins deux arguments entre guillemets")
        return False
    return True

# Récupération de données :
def get_arguments() -> list[str]:
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def print_rotated_position_on_left() -> None:
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return

    input_list = arguments
    new_list = rotate_position_on_left(input_list)
    print(', '.join(map(str, new_list)))


# Affichage :

print_rotated_position_on_left()