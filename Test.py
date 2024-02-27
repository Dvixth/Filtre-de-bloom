import math
import random

#Prendre que la partie décimal d'un nombre float
def getintpart(n):
    result=math.modf(n)
    return result[1]

#Fonction qui retourne un tableau d'élements a partir d'un fichier text
def transformt_text_into_int(E):
    with open(E, 'r') as f:
        data = f.read()
    res = [int(i) for i in data.split()]
    return res


#Fonction qui généré un theta pour les fonctions de hachage 
def theta():
    return random.random()

def generer_fonction_hachage(nbFonctionDeHachage, N):
    H = []
    for i in range(nbFonctionDeHachage):
        thetha = theta()
        H.append(thetha * N)
    return H


def filtre_de_bloom(Taille_Filtre_Bloom, nbFonctionDeHachage, elements):
    
    Bloom = [False] * Taille_Filtre_Bloom  # Initialize Bloom filter

    for element in elements:
        HachagesFonctio = generer_fonction_hachage(element, nbFonctionDeHachage, Taille_Filtre_Bloom)
        for h in HachagesFonctio:
            Bloom[h] = True
    return Bloom

def chercher_BD(Bloom,elements):
    
    return 



if __name__ == "__main__":

    hachageFonctions=generer_fonction_hachage(5,10)
    elements=[1,2,3,4,5,6,7,8,9,10]
    
    
    