#Les imports :
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

'''
Fonction qui retourne un random dans l'intervalle [0-1)
'''

def theta():
    return random.random()

'''
Fonction qui génère un tableau de fonctions de hachage, l'élement lambda x est un élement qui peut être 
fourni après, le concept c'est que les fonctions de hachage sont sauvegardé en mémoire jusqu'a ce que 
l'élement lambda x qui est dans notre cas, l'élément dans note base de donnée qui sera fournit ensuite. 
cette méthode de lambda nous permet de générer les mêmes fonctions de hachages.
Entrées : Nombre de fonction de hachage à générer, et N la taille du filtre.
sortie : h un tableau contenent les fonctions de hachage 
'''
def generer_fonctions_de_hachage(nbFonctionsDeHachage, N):
    fonctions_de_hachage = []
    for _ in range(nbFonctionsDeHachage):
        thetha = theta()  # Appeler theta() à l'intérieur de la boucle
        h = lambda x, theta=thetha, N=N: int((x * theta) * N) % N
        fonctions_de_hachage.append(h)
    return fonctions_de_hachage

'''
Fonction qui représente le Filtre de Bloom elle permet de retourner un tableau de booléens après avoir opérer sur les 
élements fournit en paramètre qui seront en guise de données de base de donnée dans notre projet.
entrée: Taille du filtre de bloom, fonctions de hachage, et un tableau d'éléments à sauvegarder.
sortie : Un vecteur de boolean une fois les opération sur le filtre sont faite (calcul des indices a mettre a 1 (Vrai) pour chaque élements et pour toutes les fonctions de hachage)
'''
def filtre_de_bloom(Taille_Filtre_Bloom, fonctions_de_hachage, elements):
    # Initialisation du filtre de bloom avec la taille définie
    Bloom = [False] * Taille_Filtre_Bloom

    # Pour chaque élément dans elements on applique les fonctions de hachage pétablie et on définit le filtre.
    for element in elements:
        for h in fonctions_de_hachage:
            Bloom[h(element)] = True
    return Bloom

'''
Fonction qui répond répond par faux si le l'élement n'existe pas dans le filtre (Cas ou y a une valeur pour une fonction 
hi qui est fausse), sinon répond Vrai/Faux (potentiellement possiblité de faux possitif ).
Entrée : Elements a chercher, les fonctions de hachage, et le filtre 
'''
def chercher_Bloom(elements, fonctions_de_hachage, filtre_bloom):
    
    faux_positifs = []

    for e in elements:
        est_present_dans_base = True
        for h in fonctions_de_hachage:
            if not filtre_bloom[h(e)]:
                est_present_dans_base = False
                break  # Sortir de la boucle interne dès qu'on trouve un élément manquant
        if est_present_dans_base:
            faux_positifs.append(e)
    return faux_positifs

'''
Fonction qui lit un fichier text qui contient des chaînes de caractères comme données, 
et les transforme en un tableau de valeurs numériques pou pour chaque mot présent dans le fichier
pour ceci il divise le mot en caractère et transforme chaque caractère en sa valeur ASCII et ensuite elle additionne 
ces valeurs et les transforme ensuite en valeur entière.
Exemple: "ABC" -> "65 66 67" -> 65+66+67
Entrée: fichier text contenant des mots séparés par des sauts de lignes
Sortie: tableau contenant de valeurs numériques pour chaque mot présent dans le fichier
'''
def text_en_num(E):
    with open(E, 'r') as f:
        lines = f.readlines()
    results = []
    for line in lines:
        if line.strip():  # Vérifie si la ligne n'est pas vide
            words = line.strip().split()  # Divise la ligne en mots
            ascii_sum = 0
            for word in words:
                ascii_values = ''.join(str(ord(char)) for char in word)
                ascii_sum += int(ascii_values)
            results.append(ascii_sum)
    return results

if __name__ == "__main__":
    
    #Les fichiers d'entrée 
    data_1 = text_en_num("MotExistant.txt") #Taille de 100 mots qui seront existant dans la base et qui serviront pour initialiser le filtre de Bloom
    data_2 = text_en_num("MotNonExistant.txt") #Taille de 100 mots qui serviront pour tester le taux de faux positifs (il existe pas réelement dans la base)

    # Liste pour stocker les données
    nb_faux_positifs = []
    nb_fonctions_hachage = []
    taille_filtre = []
    
    # Boucles pour générer les données
    for i in range(2, 9, 1):
        for j in range(100, 1100, 100):
            
            elementsExistant = data_1  
            elementsnonExistant = data_2  
            fonctions_de_hachages = generer_fonctions_de_hachage(i, j)
            
            #Filtre de bloom 
            Bloom = filtre_de_bloom(j, fonctions_de_hachages, elementsExistant)
            #Tableau les élements qui représente les faux positifs
            res = chercher_Bloom(elementsnonExistant, fonctions_de_hachages, Bloom)
              
            nb_faux_positifs.append(len(res))
            nb_fonctions_hachage.append(i)
            taille_filtre.append(j)
            
print("Le nombre de faux positif : ", nb_faux_positifs)
print("le nombre de fonction de hachage : ", nb_fonctions_hachage)
print("Taille du filtre de bloom : ", taille_filtre)
            
# Création d'une figure 3D
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Tracé en surface des données
surf = ax.plot_trisurf(nb_fonctions_hachage, taille_filtre, nb_faux_positifs, cmap='viridis', edgecolor='none')

# Étiquetage des axes
ax.set_xlabel('Nombre de fonctions de hachage', fontsize=8)
ax.set_ylabel('Taille du filtre de Bloom', fontsize=8,)
ax.set_zlabel('Nombre de faux positifs', fontsize=8)

# Ajout d'une légende
ax.legend(['Faux positifs'], loc='upper right', fontsize=10)

plt.title('Nombre de faux positifs en fonction du nombre de fonctions de hachage et de la taille du filtre de Bloom', fontsize=14)

# Ajustement de l'angle de vue
ax.view_init(elev=20, azim=30)

plt.show()