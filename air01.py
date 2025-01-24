'''Créez un programme qui découpe une chaîne de caractères en tableau en fonction du séparateur donné en 2e argument.

Votre programme devra intégrer une fonction prototypée comme ceci :
ma_fonction(string_à_couper, string_séparateur) { // syntaxe selon votre langage
	# votre algorithme
	return (tableau)
}


Exemples d’utilisation :
$> python exo.py “Crevette magique dans la mer des étoiles” “la”
Crevette magique dans 
 mer des étoiles

Afficher error et quitter le programme en cas de problèmes d’arguments.
'''

import sys

# Fonctions utilisées:
def split_chain(string_to_cut, string_separator):
    index_separator = string_to_cut.find(string_separator)
    length_separator = len(string_separator)
    list = string_to_cut.split(string_separator)
    return list

# Gestion d'erreurs :
def is_valid_length(arguments):
    if len(arguments) != 2:
        print("Erreur : Merci d'indiquer deux arguments entre guillemets")
        return False
    return True

# Récupération de données :
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :
def get_split_chain():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    string_separator = arguments[1]
    return split_chain(arguments[0], string_separator)

# Affichage :
def display():
    splited_chain = get_split_chain()
    for word in splited_chain:
        print(word)

display()
