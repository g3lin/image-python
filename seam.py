'''
Deuxième étape : Détermination de la seam optimale


A ce stade, on dispose de : 
    - une image à traiter
    - (Anthony) sa carte d'énergie

Ce fichier permet de calculer le cout des differents seams au sein d'une matrice
calculée à l'aide de la fonction calculate_cost_matrix() qui prend en parametre une image au mode L 

la fonction detect_seam() prend en parametre une matrice de cout calculée precedement et retourne le liste de tuples
La fonction calcule le chemin le plus optimal au sein de la matrice de cout et retourne une liste de tuple contenant
les x et y du pixel à supprimer
'''

from PIL import Image

def calculate_cost_matrix(image_grad):
    '''
    Cette fonction calcule une matrice de coût d'une image à partir de son
    gradient, et la retourne
    '''
    im = image_grad
    cost_matrix = []    
    pix = im.load() # on cahrge l'image

    # Calcul de la matrice des couts
    for y in range(0,im.size[1]):
        tabline = [] #on crée un nouveau tableau pour chaque ligne du tableau

        for x in range(0, im.size[0]):
            
            if y>0:
                if x-1 < 0:
                    # cas où on est à gauche de l'image
                    c2 = cost_matrix[len(cost_matrix)-1][x] 
                    c3 = cost_matrix[len(cost_matrix)-1][x+1]
                    # le cout du pixel est la somme la valeur du pixel avec le minimum du cout du pixel en haut et celui en haut à droite
                    cost = pix[x,y] + min(c2,c3)


                elif x+1 >= im.size[0]:
                    # cas où on est vers le milieu
                    c1 = cost_matrix[len(cost_matrix)-1][x-1]
                    c2 = cost_matrix[len(cost_matrix)-1][x]
                    # le cout du pixel est la somme la valeur du pixel avec le minimum du cout du pixel en haut et celui en haut à gauche
                    cost = pix[x,y] + min(c1,c2)

                else:
                    # cas où on est vers la droite
                    c1 = cost_matrix[len(cost_matrix)-1][x-1]
                    c2 = cost_matrix[len(cost_matrix)-1][x]
                    c3 = cost_matrix[len(cost_matrix)-1][x+1]
                    # le cout du pixel est la somme la valeur du pixel avec le minimum du cout du pixel en haut et celui en haut à droite et celui en haut à gauche
                    cost = pix[x,y] + min(c1,c2,c3)
            else:
                cost = pix[x,y] 
                # si on est dans la ligne du haut ( y = 0 ), on va juste mettre en cout la valeur du pixel
            # on rajoute à la ligne le cout du pixel
            tabline += [cost]

        # on rajoute à la matrice de couts la lgne deds couts
        cost_matrix += [tabline]    
    
    return cost_matrix

def detect_seam(cost_matrix):
    '''
    Cette fonction détermine la seam optimale, qui sera enlevée, à partir 
    de la matrice de coût de l'image
    '''
    seam = []
    y = len(cost_matrix)-1
    min_x_value = cost_matrix[y][0]
    min_x = 0

    # pour la ligne tout en bas de l'image 
    for x in range( len(cost_matrix[1])-1 ):
        # On cherche la valeur minimum sur toute cette ligne
        if cost_matrix[y][x] < min_x_value:
            min_x_value = cost_matrix[y][x]
            min_x = x
    x = min_x
    # On rajoute au seam le tuple du pixel à supprimer sur la ligne du bas
    seam += [(x,y)]

    # Pour toutes les autres lignes que celle du bas on va remonter
    for y in range(len(cost_matrix)-2, -1,-1):
        min_x_value = cost_matrix[y][x]
        min_x = x
        for x in range( x-1,x+2 ):
            # on choisit le minimum entre le pixel en haut celui en hait à droite et celui en haut à gauche
            if cost_matrix[y][x] < min_x_value :
                min_x_value = cost_matrix[y][x]
                min_x = x
        x = min_x
        #  une fois ce minimum au niveau des couts calculé, on ajoute cela au seam
        seam += [(x,y)]
    # une fois toutes les lignes traitées on peut retourner la liste de tuples contenant les poins à supprimer
    return seam


def main():
    '''
    Fonction principale : charge une image, calcule sa matrice de coût et détermine la seam à retirer
    '''
    # test data
    im = Image.open("1g.jpg")
    cm = calculate_cost_matrix(im)
    sm = detect_seam(cm)


if __name__ == "__main__":
    main()