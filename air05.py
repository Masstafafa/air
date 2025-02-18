import sys

# Fonctions utilisées:
def make_addition_or_substraction(numbers: list[str], addorsub: str) -> list[int]:
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

def is_valid_length(arguments: list[str]) -> bool: #vérifie qu'il y a bien deux argumens au moins
    if len(arguments) < 2:
        print("Erreur : Merci d'indiquer au moins deux nombres entiers")
        return False
    return True

def is_valid_argument(arguments: list[str]) -> bool: #vérifie que les données rentrées par l'utilisateur sont bien des chiffres
    for argument in arguments[:-1]:
        if not argument.isdigit(): 
            print("Erreur : Merci d'indiquer uniquement des nombres entiers")
            return False
    return True

def is_valid_operator(last_number: str) -> bool: #vérifie que l'on fait bien une addition ou soustraction
    list_operator = ["-", "+"]
    if last_number[0] not in list_operator:
        print("Erreur : Merci d'indiquer - ou + devant le dernier argument")
        return False
    return True
    
def is_valid_number(last_number: str) -> bool: #verifie que le dernier element soit bien un chiffre
    if not last_number[-1:].isdigit():
        print("Erreur : Le nombre après le signe doit être un entier")
        return False
    return True


# Récupération de données :
def get_arguments() -> list[str]:
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def display_result() -> None:
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    if not is_valid_argument(arguments):
        return
    
    last_number = arguments[-1]
    if not is_valid_operator(last_number):
        return
    if not is_valid_number(last_number):
        return
    
    numbers = arguments[:-1]
    result = make_addition_or_substraction(numbers, last_number)
    for number in result:
        print(number, end=' ')

        #ou print(" ".join(map(str, result)))

# Affichage :

display_result()
    
