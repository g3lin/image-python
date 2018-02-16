'''
A ce stade, on a : 
    - une image à traiter
    - sa carte d'énergie
    - une fonction (celle d'Antoine) detect_seam utilisant la carte d'énergie, et qui retourne la seam
        à enlever sous forme de liste de coordonnées
        - cette fonction s'aide d'une fonction calculate_cost qui calcule le coût d'un pixel dans l'image  

'''

from PIL import Image
from main.py import detect_seam calculate_cost

def height_redim(path_im, height):
    im = Image.open(path_im)
    #Rotation à 90° : cop (pixc)
    cop = Image.new("RGB", (im.size[1], im.size[0]))
    pix = im.load()
    pixc = cop.load()
    for j in range(im.size[1]):
        for i in range(im.size[0]):
            pixc[im.size[1]-j-1, i] = pix[i,j]
    Image.save(cop, )
    
    #Utilisation de l'algorithme d'Antoine
    while cop.size[0] > height:
        
    


def main():
    
if __name__ == "__main__":
    main() 