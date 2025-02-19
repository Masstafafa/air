import sys

# Fonctions utilisées:
def insert_last_number(numbers: list[int], number_to_insert: int) -> list[int]:
    new_list_numbers = []
    find_position = False
    for number in numbers:
        if find_position:
            new_list_numbers.append(number)
        elif number < number_to_insert:
            new_list_numbers.append(number)
        elif number > number_to_insert:
            new_list_numbers.append(number_to_insert)
            new_list_numbers.append(number)
            find_position = True
        elif number == number_to_insert:
            new_list_numbers.append(number_to_insert)
            find_position = True
    if not find_position:
        new_list_numbers.append(number_to_insert)
    return new_list_numbers

# Gestion d'erreurs :

def is_valid_length(arguments: list) -> bool: #vérifie qu'il y a bien trois argumens au moins
    if len(arguments) < 3:
        print("Erreur : Merci d'indiquer au moins trois arguments qui sont des nombres")
        return False
    return True

def is_valid_arguments(numbers: list) -> bool: #vérifie que les arguments sont bien des chiffres
    for number in numbers:
        if not number.isdigit():
            print("Erreur : Merci d'indiquer au moins trois arguments qui sont des nombres")
            return False
    return True

def is_sorted_numbers(list_to_check: list) -> bool: #verifie que les nombres sont dans le bon ordre 
    for i in range(len(list_to_check) -1):
        if int(list_to_check[i]) > int(list_to_check[i + 1]):
            print("Erreur : La liste n'est pas triée dans l'ordre croissant")
            return False
    return True

# Récupération de données :
def get_arguments() -> list:
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def display_new_sorted_numbers() -> None:
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    
    if not is_valid_arguments(arguments):
        return
    
    list_to_check = arguments[:-1] #liste a verifier sans le dernier argument qui est celui a inserer
    if not is_sorted_numbers(list_to_check):
        return
    
    numbers = list(map(int, arguments[:-1]))
    number_to_insert = int(arguments[-1])
    new_list_sorted = insert_last_number(numbers, number_to_insert)
    for number in new_list_sorted:
        print(number, end = ' ')

# Affichage :
display_new_sorted_numbers()