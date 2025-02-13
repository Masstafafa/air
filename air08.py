'''Créez un programme qui fusionne deux listes d’entiers triées en les gardant triées, 
les deux listes seront séparées par un “fusion”.

Utilisez une fonction de ce genre (selon votre langage) :
sorted_fusion(array1, array2) {
	# your algo
	return (new_array)
}


Exemples d’utilisation :
$> ruby exo.rb 10 20 30 fusion 15 25 35
10 15 20 25 30 35


Afficher error et quitter le programme en cas de problèmes d’arguments.
'''


import sys

# Fonctions utilisées:
def fusion_two_list():


# Gestion d'erreurs :

def is_valid_length(arguments): #vérifie qu'il y a bien deux argumens au moins
    if len(arguments) < 3:
        print("Erreur : Merci d'indiquer au moins deux arguments entre guillemets")
        return False
    return True

def is_valide_separator(arguments):

# Récupération de données :
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def get_removed_array():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    return remove_last_array(arguments[:-1], arguments[-1])

# Affichage :

