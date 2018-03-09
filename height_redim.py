'''
Dernière étape : Utilisation du seam carving vertical pour faire un seam carving horizontal


A ce stade, on dispose de : 
    - une image à traiter
    - (Anthony) sa carte d'énergie
    - (Antoine) une fonction calculate_cost_matrix qui détermine une matrice des coûts de l'image
    - (Antoine) une fonction detect_seam utilisant la matrice de coûts, et qui retourne la seam verticale
        à enlever sous forme de tuple de coordonnées
    - (Elie) une fonction qui enlève le seam demandé sur l'image
    - (Elie) une fonction qui décale l'image pour compenser la suppression du seam

Tout cela applique un seam carving vertical
Ce fichier permet d'appliquer un seam carving horizontal à partir du seam carving vertical déjà codé
'''

from PIL import Image
from seam import detect_seam 
from seam import calculate_cost_matrix 
from elie import remove_seam 
from dual_gradient import gradient

def height_redim(im, height, im_grad):
    '''
    Cette fonction : 
        - tourne l'image et le gradient de l'image à 90° à droite
        - applique le seam carving sur les images tournées jusqu'à ce que la hauteur voulue soit atteinte
        - re-tourne l'image et la renvoie
    '''
    rotated = im.rotate(270)
    rotated_grad = im_grad.rotate(270)
    
    # Utilisation de l'algorithme d'Antoine
    while rotated.size[0] > height:                                     # >= peut etre ?

        # Partie d'Antoine (seam.py)
        cost_matrix = calculate_cost_matrix(rotated_grad)
        seam = detect_seam(cost_matrix)

        # Partie d'Elie (elie.py) 
        rotated = remove_seam(rotated, seam)
    
    return rotated.rotate(90)



def main():
    '''
    Fonction principale
    '''
    im = Image.open("1.jpg")
    grad_anthony = gradient(im)
    im_grad = Image.open("1g.jpg")
    hr = height_redim(im, 300, im_grad)
    hr_anthony = height_redim(im, 300, im_grad)
    hr.show()
    hr_anthony.show()
    
if __name__ == "__main__":
    main() 