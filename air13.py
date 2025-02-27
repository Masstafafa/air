import json
import subprocess
from typing import Dict, List, Tuple
from pathlib import Path


# Définition des couleurs pour l'affichage
GREEN = '\033[92m'  
RED = '\033[91m'    
RESET = '\033[0m'   

# Fonctions utilitaires:
def load_tests() -> Dict[str, List[Tuple[str, str]]]:
        with open('air_tests.json', 'r') as file:
            json_tests = json.load(file)
            tests = {}
            for exercise, test_list in json_tests.items():
                tests[exercise] = [(test['command'], test['expected']) for test in test_list]
            return tests

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
                
                # Affichage du résultat(peut etre faire une fonction a part)
                message = f"{exercise_name} ({i+1}/{len(test_list)}) : {'success' if success else 'failure'}"
                if success:
                    print(f"{GREEN}{message}{RESET}")
                else:
                    print(f"{RED}{message}{RESET}")
    
    return total_success, total_tests

# Récupération de données :

def get_all_files() -> List[str]:
    current_dir = Path.cwd()
    files = []
    for file in current_dir.iterdir():
        files.append(file.name)
    return sorted(files)

# Résolution :

def display_result():
    all_exercises = get_all_files()
    
    tests = load_tests()
    
    total_success, total_tests = run_tests(all_exercises, tests)
    
    print(f"\nTotal success: ({total_success}/{total_tests})")

# Affichage :

display_result()
