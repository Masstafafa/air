import glob
import subprocess
from typing import Dict, List, Tuple, Optional, Union, Any
from pathlib import Path


# Définition des couleurs pour l'affichage
GREEN = '\033[92m'  
RED = '\033[91m'    
RESET = '\033[0m'   

# Définition des tests
def define_tests() -> Dict[str, List[Tuple[str, str]]]:
    tests = {
        "air00.py": [
            ("python3 air00.py 'bonjour les amis'", "bonjour\nles\namis"),
            ("python3 air00.py 'Ceci est un test'", "Ceci\nest\nun\ntest"),
            ("python3 air00.py 'a b c'", "a\nb\nc")
        ],
        "air01.py": [
            ("python3 air01.py 'Ceci est un test' 'un'", "Ceci est \n test"),  
            ("python3 air01.py 'La vie est belle' 'vie'", "La \n est belle")   
        ],
        "air02.py": [
            ("python3 air02.py 'je' 'test' 'des' 'trucs' ' '", "je test des trucs"),
            ("python3 air02.py 'Bonjour' 'ou' 'a'", "Bonjouraou")
        ],
        "air03.py": [
            ("python3 air03.py 1 2 3 4 5 4 3 2 1", "5"),
            ("python3 air03.py bonjour monsieur bonjour", "monsieur")
        ],
        "air04.py": [
            ("python3 air04.py 'Hello milady,   bien ou quoi ??'", "Helo milady, bien ou quoi ?"),
            ('''python3 air04.py "le code c'est pas une parrttie de pllaiisiir"''', "le code c'est pas une partie de plaisir")
            #Lorsque on a un caractere spé comme dans "c'est" il faut utiliser des guillement triples pour le definir dans python
            #On peut aussi faire un double echappement pour eviter les erreurs : \\
        ],
        "air05.py": [
            ("python3 air05.py 1 2 3 4 5 '+2'", "3 4 5 6 7"),
            ("python3 air05.py 10 11 12 13 14 '-5'", "5 6 7 8 9")
        ],
        "air06.py": [
            ("python3 air06.py 'Michel' 'Albert' 'Thérèse' 'Benoit' 't'", "Michel, Thérèse"),
            ("python3 air06.py 'Poulet' 'Saucisse' 'Patate' 'Poireau' 'a'", "Poulet")
        ],
        "air07.py": [
            ("python3 air07.py 1 3 4 2", "1 2 3 4"),
            ("python3 air07.py 10 20 30 40 50 60 70 90 33", "10 20 30 33 40 50 60 70 90")
        ],
        "air08.py": [
            ("python3 air08.py 10 20 30 'fusion' 15 25 35", "10 15 20 25 30 35"),
            ("python3 air08.py 20 30 40 'fusion' 25 35 45", "20 25 30 35 40 45")
        ],
        "air09.py": [
            ("python3 air09.py 'Michel' 'Albert' 'Thérèse' 'Benoit'", "Albert, Thérèse, Benoit, Michel"),
            ("python3 air09.py 'z' 'a' 'b'", "a, b, z")
        ],
        "air10.py": [
            ("python3 air10.py a.txt", "Hello World"),
            ("python3 air10.py b.txt", "Tu peux le faire!")
        ],
        "air11.py": [
            ("python3 air11.py O 5", "    O\n   OOO\n  OOOOO\n OOOOOOO\nOOOOOOOOO"),
            ("python3 air11.py l 4", "   l\n  lll\n lllll\nlllllll")
        ],
        "air12.py": [
            ("python3 air12.py 6 5 4 3 2 1", "1 2 3 4 5 6"),
            ("python3 air12.py 100 20 30 50 40", "20 30 40 50 100")
        ]
    }
    
    return tests


# Fonctions utilitaires:
def execute_test(command: str, expected: str) -> bool:
    process = subprocess.run(command, shell=True, 
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                           text=True, timeout=5)
    
    output = process.stdout.strip()
    
    return output == expected.strip()

def run_tests(all_exercises: List[str], tests: Dict[str, List[Tuple[str, str]]]) -> Tuple[int, int]:
    total_success = 0
    total_tests = 0
    for exercise in all_exercises:
        if exercise in tests:
            test_list = tests[exercise]
            
            # Récupérer le nom de l'exercice sans l'extension
            exercise_name = exercise[:-3]  # Enlève ".py"
            
            for i in range(len(test_list)):
                command, expected = test_list[i] 
                success = execute_test(command, expected)
                total_tests += 1

                if success:
                    total_success += 1  # Incrémente le compteur des succès
                
                # Affichage du résultat
                message = f"{exercise_name} ({i+1}/{len(test_list)}) : {'success' if success else 'failure'}"
                if success:
                    print(f"{GREEN}{message}{RESET}")
                else:
                    print(f"{RED}{message}{RESET}")
    
    return total_success, total_tests

# Récupération de données :

def list_all_files():
    current_dir = Path.cwd()
    
    print(f"Contenu du répertoire: {current_dir}")
    print("-" * 50)
    
    # Parcourir tous les éléments (fichiers et répertoires)
    for item in current_dir.iterdir():
        # Affiche le nom avec une indication si c'est un fichier ou un répertoire
        file_type = "Dossier" if item.is_dir() else "Fichier"
        print(f"{item.name} - {file_type}")

# Résolution :

'''def display_result():
    all_exercises = get_exercises()
    
    tests = define_tests()
    
    total_success, total_tests = run_tests(all_exercises, tests)
    
    print(f"\nTotal success: ({total_success}/{total_tests})")

# Affichage :

display_result()'''
list_all_files()