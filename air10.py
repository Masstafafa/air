
import sys
import os

# Fonctions utilisées:

def get_read_file(file_path: str) -> str:
    with open(file_path, 'r') as file:
        content = file.read()
    return content

# Gestion d'erreurs :

def is_valid_length(arguments: list[str]) -> bool: 
    if len(arguments) != 1:
        print("Erreur : Merci d'indiquer un seul argument qui est le nom du fichier que vous souhaitez ouvrir")
        return False
    return True

def is_valid_file(file_path: str) -> bool:
    if os.path.exists(file_path) == False:
        print("Erreur : Il n'exite aucun fichier de ce nom")
        return False
    return True

# Récupération de données :
def get_arguments() -> list[str]:
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def display_content_file() -> None:
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    
    file_path = arguments[0]
    if not is_valid_file(file_path):
        return
    
    content_file = get_read_file(file_path)
    print(content_file)


# Affichage :

display_content_file()