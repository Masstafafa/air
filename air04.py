import sys

# Fonctions utilisées:
def find_repetitive_character(arguments):
    new_string = '' #Création d'une variable pour mettre la phrase
    for i in range(len(arguments) -1): #longueur de la phrase
        current_chr = arguments[i] #on compare les lettres
        next_chr = arguments[i + 1]
        if current_chr != next_chr:
            new_string += current_chr
        
    new_string += arguments[-1] #dernière lettre
    return new_string

# Gestion d'erreurs :
def is_valid_length(arguments):
    if len(arguments) != 1:
        print("Erreur : Merci d'indiquer une seule phrase entre guillemets")
        return False
    return True

# Récupération de données :
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :
def no_repetitive_character():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    return find_repetitive_character(arguments[0])

# Affichage :
def display():
    final_string = no_repetitive_character()
    if final_string is not None:  
        print(final_string)

display()
