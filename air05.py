import sys

# Fonctions utilisées:
def make_addition_or_substraction(numbers, addorsub):
    operator = addorsub[0]
    operator_number = int(addorsub[1:]) 
    new_list_number = []

    for number in numbers:
        number = int(number)
        if operator == "-":
            number -= operator_number
        elif operator == "+":
            number += operator_number
        new_list_number.append(number)
    return new_list_number
        
# Gestion d'erreurs :

def is_valid_length(arguments): #vérifie qu'il y a bien deux argumens au moins
    if len(arguments) < 2:
        print("Erreur : Merci d'indiquer au moins deux nombres entiers")
        return False
    return True

def is_valid_argument(arguments): #vérifie que les données rentrées par l'utilisateur sont bien des chiffres
    for arg in arguments[:-1]:
        if not arg.isdigit(): 
            print("Erreur : Merci d'indiquer uniquement des nombres entiers")
            return False
    return True

def is_valid_operator(last_argument): #vérifie que l'on fait bien une addition ou soustraction avec un chiffre
    list_operator = ["-", "+"]
    if last_argument[0] not in list_operator:
        print("Erreur : Merci d'indiquer - ou + devant le dernier argument")
        return False
    
    if not last_argument[1:].isdigit():
        print("Erreur : Le nombre après le signe doit être un entier")
        return False
    return True


# Récupération de données :
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def get_result():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    if not is_valid_argument(arguments):
        return
    if not is_valid_operator(arguments[-1]):
        return
    return make_addition_or_substraction(arguments[:-1], arguments[-1])


# Affichage :
def display():
    result = get_result()
    if result is not None:
        for num in result:
            print(num, end=' ')

display()

    
