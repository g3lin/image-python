'''
A ce stade, on a : 
    - une image à traiter
    - sa carte d'énergie (Anthony)
    - une fonction (celle d'Antoine) detect_seam utilisant la carte d'énergie, et qui retourne la seam
        à enlever sous forme de liste de coordonnées
        - cette fonction s'aide d'une fonction calculate_cost qui calcule le coût d'un pixel dans l'image  

'''

from PIL import Image
from seam import detect_seam calculate_cost_matrix 
from elie import remove_seam shift_left

def height_redim(im, height, im_grad):
    rotated = im.rotate(270)
    rotated_grad = im_grad.rotate(270)
    
    # Utilisation de l'algorithme d'Antoine
    while rotated.size[0] > height: # >= peut etre ?
        cost_matrix = calculate_cost_matrix(rotated_grad)
        seam = detect_seam(cost_matrix)
        rotated = remove_seam(rotated, seam)
        rotated = shift_left(rotated, 1)
    
    return rotated.rotate(90)



def main():
    im = Image.open("../1.jpg")
    hr = height_redim(im, 300)
    return hr
    
if __name__ == "__main__":
    main() 