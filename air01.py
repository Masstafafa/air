import sys

# Fonctions utilisées:
def split_chain(string_to_cut, string_separator):
    list = []
    while string_separator in string_to_cut:
        index_separator = string_to_cut.find(string_separator)
        length_separator = len(string_separator)
        list.append(string_to_cut[:index_separator])
        string_to_cut = string_to_cut[(index_separator + length_separator):]
    list.append(string_to_cut) 
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

'''
solution avec boucle for
mieux vaut utiliser while car
Elle est plus naturelle pour cette tâche (continuer tant qu'on trouve un séparateur)
Elle est plus lisible et intuitive pour d'autres développeurs
Elle ne nécessite pas de compter les séparateurs à l'avance

La boucle for fonctionne aussi mais ajoute une étape supplémentaire (count) qui n'est pas nécessaire.

list = []
   nb_separators = string_to_cut.count(string_separator)
   
   for i in range(nb_separators):
       index_separator = string_to_cut.find(string_separator)
       length_separator = len(string_separator)
       list.append(string_to_cut[:index_separator])
       string_to_cut = string_to_cut[(index_separator + length_separator):]
   
   list.append(string_to_cut)
   return list
   '''