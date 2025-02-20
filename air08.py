import sys

# Fonctions utilisées:
def is_sorted(list: list[str]) -> bool:
    for i in range(len(list)-1):
        if int(list[i]) > int(list[i+1]): 
            print("Erreur : Merci de trier les listes dans l'ordre croissant")
            return False
    return True

def is_digit(list: list[str]) -> bool:
    for argument in list:
        if not argument.isdigit():
            print("Erreur : Merci d'indiquer uniquement des nombres")
            return False
    return True


def fusion_two_list(list_1: list, list_2: list) -> list:
    fusioned_list = []
    i = 0  # index list 1
    j = 0  # index list 2
    for _ in range(len(list_1) + len(list_2)):
        if i < len(list_1) and j < len(list_2):
            if int(list_1[i]) <= int(list_2[j]):
                fusioned_list.append(list_1[i])
                i += 1
            else:
                fusioned_list.append(list_2[j])
                j += 1
        elif i < len(list_1):
            fusioned_list.append(list_1[i])
            i += 1
        elif j < len(list_2):
            fusioned_list.append(list_2[j])
            j += 1
            
    return fusioned_list

# Gestion d'erreurs :

def is_valid_length(arguments: list) -> bool: #vérifie qu'il y a bien trois arguments au moins
    if len(arguments) < 3:
        print("Erreur : Merci d'indiquer au moins trois arguments")
        return False
    return True

def is_valid_separator(separator: int) -> bool: #verifie qu'il y a bien fusion une seule fois
    if separator != 1:
        print("Erreur : Merci de mettre le mot 'fusion' en séparateur, une seule fois")
        return False
    return True

def is_valid_lists(index_separator: int, arguments_length: int) -> bool: #verifie qu'il y a bien deux listes autour de fusion
    if index_separator == 0 :
        print("Erreur : Merci d'indiquer au moins un nombre avant 'fusion'")
        return False
    elif index_separator == (arguments_length - 1):
        print("Erreur : Merci d'indiquer au moins un nombre apres 'fusion'")
        return False
    return True

def is_list_numbers(list_1: list, list_2: list) -> bool: #verifie que les listes autour de fusion sont bien des nombres 
    return is_digit(list_1) and is_digit(list_2)

def is_list_sorted(list_1: list, list_2: list) -> bool: #verifie si les listes sont tries  
    return is_sorted(list_1) and is_sorted(list_2)

# Récupération de données :
def get_arguments() -> list:
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def display_two_list_fusioned() -> None:
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    
    separator = arguments.count('fusion')
    if not is_valid_separator(separator):
        return
    
    index_separator = arguments.index('fusion')
    arguments_length = len(arguments)
    if not is_valid_lists(index_separator, arguments_length):
        return
    
    list_1 = arguments[0:index_separator] 
    list_2 = arguments[index_separator + 1:]
    if not is_list_numbers(list_1, list_2):
        return
    
    if not is_list_sorted(list_1, list_2):
        return
    
    new_list_fusioned = fusion_two_list(list_1, list_2)
    print(' '.join(map(str, new_list_fusioned)))
    

# Affichage :

display_two_list_fusioned()