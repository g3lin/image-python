'''
A ce stade, on a : 
    - une image à traiter
    - sa carte d'énergie (Anthony)
    - une fonction (celle d'Antoine) detect_seam utilisant la carte d'énergie, et qui retourne la seam
        à enlever sous forme de liste de coordonnées
        - cette fonction s'aide d'une fonction calculate_cost qui calcule le coût d'un pixel dans l'image  

'''

from PIL import Image
from seam import main as seam_carving # seam_carving

def height_redim(im, height):
    rotated = im.rotate(270)
    
    # Utilisation de l'algorithme d'Antoine
    while rotated.size[0] > height: # >= peut etre ?
        seam_carving(rotated)
    
    return rotated.rotate(90)



def main():
    im = Image.open("../1.jpg")
    hr = height_redim(im, 300)
    return hr
    
if __name__ == "__main__":
    main() 