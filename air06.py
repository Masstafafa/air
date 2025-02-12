'''Créez un programme qui supprime d’un tableau tous les éléments qui ne contiennent pas une autre chaîne de caractères.

Utilisez une fonction de ce genre (selon votre langage) :
ma_fonction(array_de_strings, string) {
	# votre algorithme
	return (nouvel_array_de_strings)
}


Exemples d’utilisation :
$> python exo.py “Michel” “Albert” “Thérèse” “Benoit” “t”
Michel

$> python exo.py “Michel” “Albert” “Thérèse” “Benoit” “a”
Michel, Thérèse, Benoit



Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

import sys

# Fonctions utilisées:
def remove_last_array(strings, remove_string):
    new_string = [] #creation d'une variable pour la nouvelle phrase

    for word in strings:  
        if remove_string not in word:  
            new_string.append(word)
    return new_string

# Gestion d'erreurs :

def is_valid_length(arguments): #vérifie qu'il y a bien deux argumens au moins
    if len(arguments) < 2:
        print("Erreur : Merci d'indiquer au moins deux arguments entre guillemets")
        return False
    return True

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
def display():
    new_array = get_removed_array()
    if new_array is not None:
        for word in new_array:
            print(word, end=' ')
 
display()