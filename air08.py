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
def fusion_two_list(list_1, list_2):
    fusioned_list = []
    i = 0 #index list 1
    j = 0 #index list 2
    while i < len(list_1) and j < len(list_2):
        if int(list_1[i]) <= int(list_2[j]):
            fusioned_list.append(list1[i])
            i += 1
        else:
            fusioned_list.append(list_2[j])
            j += 1


# Gestion d'erreurs :

def is_valid_length(arguments): #vérifie qu'il y a bien deux argumens au moins
    if len(arguments) < 3:
        print("Erreur : Merci d'indiquer au moins deux arguments entre guillemets")
        return False
    return True

def is_valid_separator(arguments): #verifie qu'il y a bien fusion une seule fois
    separator = arguments.count('fusion')
    if separator != 1:
        print("Erreur : Merci de mettre le mot 'fusion' en séparateur, une seule fois")
        return False
    return True

def is_valid_arguments(arguments): #verifie qu'il y a bien deux listes autour de fusion
    index_separator = arguments.index('fusion')
    arguments_length = len(arguments)
    if index_separator == 0 :
        print("Erreur : Merci d'indiquer au moins un nombre avant 'fusion'")
        return False
    elif index_separator == (arguments_length - 1):
        print("Erreur : Merci d'indiquer au moins un nombre apres 'fusion'")
        return False
    return True

def is_list_numbers(arguments): #verifie que les listes autour de fusion sont bien des nombres 
    index_separator = arguments.index('fusion')
    list_1 = arguments[0:index_separator] 
    list_2 = arguments[index_separator + 1:]
    for argument in list_1:
        if not argument.isdigit():
            print("Erreur : Merci d'indiquer uniqement des nombres")
            return False
    for argument in list_2:
        if not argument.isdigit():
            print("Erreur : Merci d'indiquer uniqement des nombres")
            return False
    return True

def is_list_sorted(arguments): #verifie si les listes sont tries
    index_separator = arguments.index('fusion')
    list_1 = arguments[0:index_separator]
    list_2 = arguments[index_separator + 1:]   
    for i in range(len(list_1)-1):
        if int(list_1[i]) > int(list_1[i+1]): 
            print("Erreur : Merci de trier la premiere liste")
            return False
    for i in range(len(list_2)-1):
        if int(list_2[i]) > int(list_2[i+1]): 
            print("Erreur : Merci de trier la derniere liste")
            return False
    return True

# Récupération de données :
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def display_two_list_fusioned():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    if not is_valid_separator(arguments):
        return
    if not is_valid_arguments(arguments):
        return
    if not is_list_numbers(arguments):
        return
    if not is_list_sorted(arguments):
        return
    index_separator = arguments.index('fusion')
    list_1 = arguments[0:index_separator]
    list_2 = arguments[index_separator + 1:]
    new_list_fusioned = fusion_two_list(list_1, list_2)
    if new_list_fusioned is not None:
        for number in new_list_fusioned:
            print(number, end=' ')

# Affichage :

display_two_list_fusioned()