import sys

# Fonctions utilisées:
def find_intruder(arguments):
    # string_with_no_intruder = [] -> dans le cas ou on veut aller plus loin et si il y a plusieurs arguments uniques : bien penser à increment la liste avec .append()
    for arg in arguments: #check tous les arguments 
        count = 0 #compteur de l'argument si il y en a qu'un le retourner sinon ne pas mettre à jour la variable string with no intruder
        for check_arg in arguments: #on check tous les arguments
            if arg == check_arg:
                count += 1 
        
        if count == 1:  
            return arg
        

# Gestion d'erreurs :
def is_valid_length(arguments):
    if len(arguments) < 3:
        print("Erreur : Merci d'indiquer un minimum de trois arguments avec deux arguments les mêmes")
        return False
    return True

# Récupération de données :
def get_arguments():
    arguments = sys.argv[1:]
    return arguments

# Résolution :
def get_intruder():
    arguments = get_arguments()
    if not is_valid_length(arguments):
        return
    return find_intruder(arguments)

# Affichage :
def display():
    intruder = get_intruder()
    if intruder is not None:  # Vérifie si on a un résultat
        print(intruder)

display()
