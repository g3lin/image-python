'''
A ce stade, on a : 
    - une image à traiter
    - sa carte d'énergie (Anthony)
    - une fonction (celle d'Antoine) detect_seam utilisant la carte d'énergie, et qui retourne la seam
        à enlever sous forme de liste de coordonnées
        - cette fonction s'aide d'une fonction calculate_cost qui calcule le coût d'un pixel dans l'image  

'''

from PIL import Image
from seam.py import seam_carving

def height_redim(im, height):
    rotated = rotate90d(im)
    
    #Utilisation de l'algorithme d'Antoine
    while cop.size[0] > height: # >= peut etre ?
        seam_carving(rotated)
    
    return rotated90g(rotated)
    
def rotate90d(im):
    '''
    Applique une rotation à 90° vers la droite à une image , puis la retourne 
    '''
    cop = Image.new("RGB", (im.size[1], im.size[0]))
    pix = im.load()
    pixc = cop.load()
    for j in range(im.size[1]):
        for i in range(im.size[0]):
            pixc[im.size[1]-j-1, i] = pix[i,j]
    return cop

def rotate90g(im):
    '''
    Applique une rotation à 90° vers la gauche à une image, puis la retourne
    '''
    cop = Image.new("RGB", (im.size[1], im.size[0]))
    pix = im.load()
    pixc = cop.load()
    for j in range(im.size[1]):
        for i in range(im.size[0]):
            pixc[j, im.size[0]-i-1] = pix[i,j]
    return cop

        
    


def main(im, height):
    return height_redim(im, height)
    
if __name__ == "__main__":
    main() 