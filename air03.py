import sys
from typing import Any, Optional

# Fonctions utilisées:

def find_single_argument(arguments: list[Any]) -> Optional[str]:
    # list_with_single_argument = [] -> dans le cas ou on veut aller plus loin et si 
    # il y a plusieurs arguments uniques : bien penser à incrementer la liste avec .append()
    for argument in arguments: #check tous les arguments 
        count = 0 #compteur de l'argument 
        for check_argument in arguments: #on check tous les arguments
            if argument == check_argument:
                count += 1 
        if count == 1:  
            return argument

# Gestion d'erreurs :

def is_valid_length(arguments: list[Any]) -> bool:
    if len(arguments) < 3:
        print("Erreur : Merci d'indiquer un minimum de trois arguments avec deux arguments les mêmes")
        return False
    return True

# Récupération de données :

def get_arguments() -> list[Any]:
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def display_single_argument() -> None:
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    
    single_argument = find_single_argument(arguments)
    if single_argument is None:
        print("Pas d'intrus trouvé")
    else:
        print(single_argument)


# Affichage :

display_single_argument()