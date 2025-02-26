import sys

# Fonctions utilisées:
def remove_last_array(strings: list[str], remove_string: str) -> list[str]:
    new_string = [] #creation d'une variable pour la nouvelle phrase
    
    for word in strings:
        found = False    # Pour indiquer si on trouve remove_string dans le mot
        
        # On ne vérifie que jusqu'à la position qui permet de contenir remove_string
        for i in range(len(word) - len(remove_string) + 1):
            match = True 
            
            # On vérifie chaque caractère de remove_string
            for j in range(len(remove_string)):
                if word[i + j] != remove_string[j]:
                    match = False
                    break
            if match:
                found = True
                break
        if not found:
            new_string.append(word)
    return new_string

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

def print_removed_array() -> None:
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    
    strings = arguments[:-1]
    remove_string = arguments[-1]
    new_array = remove_last_array(strings, remove_string)
    print(", ".join(map(str, new_array)))

# Affichage :

print_removed_array()
