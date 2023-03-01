import re
from molar_dict import element_weights

def parse_formula(formula):
    elements = []
    counts = []
    current_element = ""
    current_count = ""
    for char in formula:
        if char.isupper():
            if current_element != "":
                elements.append(current_element)
                counts.append(int(current_count) if current_count != "" else 1)
                current_count = ""
            current_element = char
        elif char.islower():
            current_element += char
        elif char.isdigit():
            current_count += char
    if current_element != "":
        elements.append(current_element)
        counts.append(int(current_count) if current_count != "" else 1)
    return elements, counts

def calculate_molecular_weight(formula):
    elements, counts = parse_formula(formula)
    total_weight = 0
    for i in range(len(elements)):
        element_weight = element_weights.get(elements[i])
        if element_weight is not None:
            total_weight += element_weight * counts[i]
    return total_weight

formula = input("Enter a chemical formula: ")
weight = calculate_molecular_weight(formula)
print(f"The molecular weight of {formula} is {round(weight,2)} u.")
print("Figure has been rounded off to 2 decimal digits.")


