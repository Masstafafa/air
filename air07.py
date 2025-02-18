import sys

# Fonctions utilisées:
def insert_last_number(numbers, last_number):
    new_numbers = [] #on convertit les arguments en chiffres
    for number in numbers:
        new_numbers.append(int(number))
    number_to_insert = int(last_number) #convertit le dernier chiffre a inserer
    new_list_sorted = [] #creation d'une liste pour la nouvelle liste triée
    inserted_number = False
    
    for number in new_numbers:
        if inserted_number == True:
            new_list_sorted.append(number)
        elif number_to_insert > number: #compare le nombre a inserer avec celui de la boucle
            new_list_sorted.append(number)
        elif number_to_insert < number:
            inserted_number = True
            new_list_sorted.append(number_to_insert) #insere le nombre si il est plus petit que celui qu'on regarde
            new_list_sorted.append(number) #et insere le nombre que l'on compare apres
        elif number_to_insert == number:
            new_list_sorted.append(number)
            inserted_number = True
    if inserted_number == False: #si le nombre n'est jamais insere il va a la fin de la liste
        new_list_sorted.append(number_to_insert)
    return new_list_sorted

# Gestion d'erreurs :

def is_valid_length(arguments): #vérifie qu'il y a bien trois argumens au moins
    if len(arguments) < 3:
        print("Erreur : Merci d'indiquer au moins trois arguments qui sont des nombres")
        return False
    return True

def is_valid_arguments(arguments): #vérifie que les arguments sont bien des chiffres
    for argument in arguments:
        if not argument.isdigit():
            print("Erreur : Merci d'indiquer au moins trois arguments qui sont des nombres")
            return False
    return True

def is_sorted_arguments(arguments): #verifie que les nombres sont dans le bon ordre
    list_to_check = arguments[:-1] #liste a verifier sans le dernier argument qui est celui a inserer
    for i in range(len(list_to_check)-1):
        if int(list_to_check[i]) > int(list_to_check[i+1]):
            print("Erreur : La liste n'est pas triée dans l'ordre croissant")
            return False
    return True

# Récupération de données :
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def display_new_sorted_numbers():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    if not is_valid_arguments(arguments):
        return
    if not is_sorted_arguments(arguments):
        return
    new_list_sorted = insert_last_number(arguments[:-1], arguments[-1])#ajouter une variable 
    #ou pas pour les parametres? 
    if new_list_sorted is not None:
        for number in new_list_sorted:
            print(number, end=' ')

# Affichage :
display_new_sorted_numbers()