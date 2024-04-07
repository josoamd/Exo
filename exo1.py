# from itertools import product
# from sympy.logic.boolalg import truth_table, simplify_logic

def eval_func(func, variables):
    """
    Evaluate a logical function with given variable values.
    """
    return func.subs(variables)

def main():
    # Entrée de la fonction logique
    func = input("Entrez la fonction logique en utilisant les variables 'A', 'B', 'C', etc. : ")
    
    # Liste des variables dans la fonction logique
    variables = sorted(set(symbol for symbol in func if symbol.isalpha()))
    
    # Générer toutes les combinaisons possibles de valeurs binaires pour les variables
    truth_values = list(product([0, 1], repeat=len(variables)))
    
    # Affichage de l'en-tête de la table de vérité
    print("Table de vérité :")
    print(" | ".join(variables + [func]))
    print("-" * (len(variables) * 3 + len(func) + 1))
    
    # Évaluation de la fonction logique pour chaque combinaison de valeurs
    for values in truth_values:
        assignment = dict(zip(variables, values))
        result = eval_func(func, assignment)
        print(" | ".join(str(value) for value in values + (result,)))
    
    # Calcul des formes canoniques
    logic_expr = truth_table(func, variables)
    first_canonical = simplify_logic(logic_expr, form='dnf')
    second_canonical = simplify_logic(logic_expr, form='cnf')
    
    # Affichage des formes canoniques
    print("\nForme canonique (DNF) : ", first_canonical)
    print("Forme canonique (CNF) : ", second_canonical)

if __name__ == "__main__":
    main()
