import random

# Fonction qui génère un theta pour les fonctions de hachage 
def theta():
    return random.random()

'''
Fonction qui génère un tableau de fonctions de hachage pour un élément e lambdas passé en paramètre après  
Entrées : element e, nb de fonction de hachage à générer, et N la taille du filtre
sortie : h un tableau contenent les résultats des fonction de hachage 
'''
def generer_fonctions_de_hachage(nbFonctionsDeHachage, N):
    fonctions_de_hachage = []
    for _ in range(nbFonctionsDeHachage):
        thetha = theta()
        h = lambda x, theta=thetha, N=N: int((x * theta) * N) % N
        fonctions_de_hachage.append(h)
    return fonctions_de_hachage

'''
Fonction qui représente le Filtre de bloom elle permet de retourner un tableau de booléens
entrée: Taille du filtre de bloom, fonctions de hachage, et un tableau d'éléments à sauvegarder 
sortie : un tableau de booléens qui représente les valeurs une fois le filtre appliqué 
'''
def filtre_de_bloom(Taille_Filtre_Bloom, fonctions_de_hachage, elements):
    # Initialisation du filtre de bloom avec la taille définie
    Bloom = [False] * Taille_Filtre_Bloom

    # Pour chaque élément dans elements on applique les fonctions de hachage pétablie et on définit le filtre.
    for element in elements:
        for h in fonctions_de_hachage:
            print(h(element))
            Bloom[h(element)] = True
    return Bloom

def chercher_Bloom(elements,fonctions_de_hachage,filtre_bloom):
    resultBool=False
    return 

def transform_text_into_int(E):
    with open(E, 'r') as f:
        data = f.read()
    res = [int(i) for i in data.split()]
    return res

if __name__ == "__main__":
    
    # Nombre de fonctions de hachage à générer
    nbFonctionsDeHachage = 3
    
    # Taille du filtre de bloom (This will be changed to be an input later)
    Taille_Filtre_Bloom = 10
    
    # Générer les fonctions de hachage
    fonctions_de_hachage = generer_fonctions_de_hachage(nbFonctionsDeHachage, Taille_Filtre_Bloom)
    
    elementsExistant =  [1, 2, 3, 4] 
    elementsnonExistant = [5, 6, 7, 8]
    
    

        
    
    
    

    
'''  # Éléments à sauvegarder dans le filtre de Bloom

    # Appliquer le filtre de Bloom
    result = filtre_de_bloom(Taille_Filtre_Bloom, fonctions_de_hachage, elementsExistant)
    
    elementsnonExistant = [5, 6, 7, 8]

    # Appliquer le filtre de Bloom
    result = filtre_de_bloom(Taille_Filtre_Bloom, fonctions_de_hachage, elements)

    # Afficher le résultat
    print(result)
'''