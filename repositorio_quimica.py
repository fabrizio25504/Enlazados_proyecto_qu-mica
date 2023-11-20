from rdkit import Chem


Sharp=2
Principal=6
Difusse=10
Fundamental=14
valencia = 0
def valencia_function(S,P,D,F,numero_atomico):

  if numero_atomico == 1 or numero_atomico == 2:
      valencia = numero_atomico
  
      return valencia
  if S == 1 :
    if numero_atomico <= 2 :
      valencia = numero_atomico
      print(f"la valencia es :{valencia}")
      return valencia
    numero_atomico = numero_atomico - Sharp
  if F == 1 :
    numero_atomico = numero_atomico - Fundamental
    if numero_atomico <= 0 :
      valencia = Sharp
  
      return valencia
  if D == 1 :
    numero_atomico = numero_atomico - Difusse
    if numero_atomico <= 0 :
      valencia = Sharp
   
      return valencia
  if P == 1 :
    valencia = numero_atomico
    valencia = valencia + Sharp
   
    return valencia

def numero_atom(numero_atomico):
    if numero_atomico <= 2 :
        valencia = numero_atomico
        return valencia
    elif numero_atomico > 2 and numero_atomico <= 10 :
        valencia=numero_atomico-2
        return valencia
    elif numero_atomico > 10 and numero_atomico <= 18:
        valencia = numero_atomico-10
        return valencia
    elif numero_atomico > 18 and numero_atomico <= 36:
        numero_atomico = numero_atomico-18
        return (valencia_function(1,1,1,0,numero_atomico))
    elif numero_atomico > 36 and numero_atomico <= 54:
        numero_atomico = numero_atomico-36
        return (valencia_function(1,1,1,0,numero_atomico))
    elif numero_atomico > 54 and numero_atomico <= 86:
        numero_atomico = numero_atomico-54
        return (valencia_function(1,1,1,1,numero_atomico))
    elif numero_atomico == 87 or numero_atomico == 88:
        numero_atomico = numero_atomico-86
        return (valencia_function(0,0,0,0,numero_atomico))


electronegatividades = { "H": 2.20, "Li": 0.98, "Na": 0.93, "K": 0.82, "Rb": 0.82,
                        "Cs": 0.79, "Fr": 0.70, "Be": 1.57, "Mg": 1.31, "Ca": 1.00,
                        "Sr": 0.95, "Ba": 0.89, "Ra": 0.90, "B": 2.04, "Al": 1.61,
                        "Ga": 1.81, "In": 1.78, "Tl": 1.62, "C": 2.55, "Si": 1.90,
                        "Ge": 2.01, "Sn": 1.96, "Pb": 1.87, "N": 3.04, "P": 2.19,
                        "As": 2.18, "Sb": 2.05, "Bi": 2.02, "O": 3.44, "S": 2.58,
                        "Se": 2.55, "Te": 2.10, "Po": 2.00, "F": 3.98, "Cl": 3.16, "Br": 2.96, "I": 2.66, "At": 2.20 }


tabla_periodica = Chem.GetPeriodicTable() 
Nombre_elemento = []
for x in range(1, 21):
    Nombre_elemento.append(tabla_periodica.GetElementSymbol(x))

#print(Nombre_elemento)


elementos_quimicos = {}

for elemento, electronegatividad in electronegatividades.items():
    elementos_quimicos[elemento] = {
        'nombre': tabla_periodica.GetElementName(tabla_periodica.GetAtomicNumber(elemento)),  
        'numero': tabla_periodica.GetAtomicNumber(elemento),
        'electroV':numero_atom(tabla_periodica.GetAtomicNumber(elemento)),
        'electroN': electronegatividad
    }

print(elementos_quimicos)


#help(Chem)