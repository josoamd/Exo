# Demandez à l'utilisateur d'entrer l'expression logique
expression = input("Entrez l'expression logique : ")

# Demandez les noms des variables impliquées dans l'expression
variable_names = input("Entrez les noms des variables (séparés par des espaces) : ").split()

# Génère toutes les combinaisons possibles de valeurs de vérité pour ces variables
def generate_combinations(variables):
    num_vars = len(variables)
    for i in range(2 ** num_vars):
        values = {var: (i >> j) & 1 for j, var in enumerate(variables)}
        yield values

# Évalue l'expression logique pour chaque combinaison et affiche les résultats
def evaluate_expression(expression, values):
    return eval(expression, values)

def main():
    truth_table = []
    for values in generate_combinations(variable_names):
        result = evaluate_expression(expression, values)
        truth_table.append(list(values.values()) + [result])

    # Affiche la table de vérité
    print("\nTable de Vérité :")
    for row in truth_table:
        print(*row)

    # Forme canonique (première forme)
    print("\nForme Canonique (première forme) :")
    print(Or(Not(p), q))

    # Forme canonique (seconde forme)
    print("\nForme Canonique (seconde forme) :")
    print(And(Or(Not(p), q), Or(p, Not(q))))

if __name__ == "__main__":
    main()
