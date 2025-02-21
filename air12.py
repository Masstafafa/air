
import sys

# Fonctions utilisées:

def quick_sort(numbers: list[int], left: int = 0, right: int = None) -> None:
    if right is None:
        right = len(numbers) - 1
        
    if left < right:
        partition_pos = partition(numbers, left, right)
        quick_sort(numbers, left, partition_pos - 1)
        quick_sort(numbers, partition_pos + 1, right)

def partition(numbers: list[int], left: int, right: int) -> int:
    pivot = numbers[right]
    i = left - 1
    
    for j in range(left, right):
        if numbers[j] <= pivot:
            i += 1
            numbers[i], numbers[j] = numbers[j], numbers[i]
    
    numbers[i + 1], numbers[right] = numbers[right], numbers[i + 1]
    return i + 1
            
# Gestion d'erreurs :

def is_valid_length(arguments: list[str]) -> bool: 
    if len(arguments) < 2:
        print("Erreur : Merci d'indiquer deux arguments qui doivent etre des nombres entiers")
        return False
    return True

def is_digit(arguments: list[str]) -> bool:
    for argument in arguments:
        if not argument.isdigit():
            print("Erreur : Merci d'indiquer uniquement des nombres entiers")
            return False
    return True

# Récupération de données :

def get_arguments() -> list[str]:
    arguments = sys.argv[1:]
    return arguments

# Résolution :

def display_list_quick_sorted() -> None:
    arguments = get_arguments()

    if not is_valid_length(arguments):
        return

    if not is_digit(arguments):
        return
    

    numbers = list(map(int, arguments))
    quick_sort(numbers)  
    print(" ".join(map(str, numbers)))  

# Affichage :

display_list_quick_sorted()
