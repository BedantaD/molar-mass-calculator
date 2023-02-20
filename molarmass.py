import re

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
    element_weights = {
        "H": 1.008,
        "He": 4.003,
        "Li": 6.941,
        "Be": 9.012,
        "B": 10.81,
        "C": 12.01,
        "N": 14.01,
        "O": 16.00,
        "F": 19.00,
        "Ne": 20.18,
        'Na': 22.99,
        'Mg': 24.31,
        'Al': 26.98,
        'Si': 28.09,
        'P': 30.97,
        'S': 32.06,
        'Cl': 35.45,
        'K': 39.10,
        'Ca': 40.08,
        'Sc': 44.96,
        'Ti': 47.87,
        'V': 50.94,
        'Cr': 52.00,
        'Mn': 54.94,
        'Fe': 55.85,
        'Co': 58.93,
        'Ni': 58.69,
        'Cu': 63.55,
        'Zn': 65.38,
        'Ga': 69.72,
        'Ge': 72.63,
        'As': 74.92,
        'Se': 78.96,
        'Br': 79.90,
        'Kr': 83.80,
        'Rb': 85.47,
        'Sr': 87.62,
        'Y': 88.91,
        'Zr': 91.22,
        'Nb': 92.91,
        'Mo': 95.94,
        'Tc': 98.00,
        'Ru': 101.1,
        'Rh': 102.9,
        'Pd': 106.4,
        'Ag': 107.9,
        'Cd': 112.4,
        'In': 114.8,
        'Sn': 118.7,
        'Sb': 121.8,
        'Te': 127.6,
        'I': 126.9,
        'Xe': 131.3,
        'Cs': 132.9,
        'Ba': 137.3,
        'La': 138.9,
        'Ce': 140.1,
        'Pr': 140.9,
        'Nd': 144.2,
        'Pm': 145.0,
        'Sm': 150.4,
        'Eu': 152.0,
        'Gd': 157.3,
        'Tb': 158.9,
        'Dy': 162.5,
        'Ho': 164.9,
        'Er': 167.3,
        'Tm': 168.9,
        'Yb': 173.0,
        'Lu': 175.0,
        'Hf': 178.5,
        'Ta': 180.9,
        'W': 183.8,
        'Re': 186.2,
        'Os': 190.2,
        'Ir': 192.2,
        'Pt': 195.1,
        'Au': 197.0,
        'Hg': 200.6,
        'Tl': 204.4,
        'Pb': 207.2,
        'Bi': 208.98,
        'Th': 232.04,
        'Pa': 231.04,
        'U': 238.03,
        'Np': 237.05,
        'Pu': 244.06,
        'Am': 243.06,
        'Cm': 247.07,
        'Bk': 247.07,
        'Cf': 251.08,
        'Es': 252.08,
        'Fm': 257.10,
        'Md': 258.10,
        'No': 259.10,
        'Lr': 262.11,
        'Rf': 267.12,
        'Db': 270.13,
        'Sg': 271.13,
        'Bh': 270.13,
        'Hs': 277.15,
        'Mt': 276.15,
        'Ds': 281.17,
        'Rg': 280.17,
        'Cn': 285.18,
        'Nh': 284.18,
        'Fl': 289.19,
        'Mc': 288.19,
        'Lv': 293.20,
        'Ts': 294.21,
        'Og': 294.21
    }
    elements, counts = parse_formula(formula)
    total_weight = 0
    for i in range(len(elements)):
        element_weight = element_weights.get(elements[i])
        if element_weight is not None:
            total_weight += element_weight * counts[i]
    return total_weight

formula = input("Enter a chemical formula: ")
weight = calculate_molecular_weight(formula)
print(f"The molecular weight of {formula} is {round(weight,2)} g/mol.")
print("Figure has been rounded off to 2 decimal digits.")


