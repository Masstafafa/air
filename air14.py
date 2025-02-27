import sys
# Fonctions utilitaires :

def get_answer():
    with open('aaa.txt', 'r') as file:
        contenu = file.read()
    return contenu

# Gestion d'erreurs :

def is_valid_length(arguments):
    if len(arguments) != 0:
        print("Erreur : Merci de n'indiquer que le nom du programmme sans argument")
        return False
    return True
    
# Récupération de données :

def get_arguments() -> list[str]:
    arguments = sys.argv[1:]
    return arguments

# Résolution :  

def display_answer():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return

    answer = get_answer()
    print(f"J’ai terminé l’Épreuve de l’air et c’était {answer}")

# Affichage :

display_answer()