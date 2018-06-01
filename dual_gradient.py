# -*- coding: utf-8 -*-
'''
Première étape : Détermination de la carte d'énergie de l'image (gradient)


A ce stade, on dispose de : 
    - une image à traiter

Après avoir essayé différents gradients (Prewitt et Sobel), nous avons
décidé d'utiliser un dual gradient.
Ce fichier permet de déterminer et afficher (pour l'instant) le gradient
de l'image donnée
'''

from PIL import Image
import math
def gradient(im):
    '''
    Affiche (pour l'instant) le dual gradient de l'image passée en paramètre.
    Cette fonction utilise les fonctions décrites dans le lien suivant :
    https://www.datasciencecentral.com/profiles/blogs/seam-carving-using-dynamic-programming-to-implement-context-aware

    '''
    im1 = im.load()
    im2 = Image.new('L', (im.size[0], im.size[1]))
    im3 = im2.load()
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            xpl = (x-1)%im.size[0]
            xpr = (x+1)%im.size[0]
            ypu = (y-1)%im.size[1]
            ypd = (y+1)%im.size[1]
            drx = im1[xpl, y][0] - im1[xpr, y][0]
            dgx = im1[xpl, y][1] - im1[xpr, y][1]
            dbx = im1[xpl, y][2] - im1[xpr, y][2]
            dry = im1[x, ypu][0] - im1[x, ypd][0]
            dgy = im1[x, ypu][1] - im1[x, ypd][1]
            dby = im1[x, ypu][2] - im1[x, ypd][2]
            G = round(math.sqrt(drx**2+dgx**2+dbx**2+dry**2+dgy**2+dby**2))
            im3[x,y] = (G,)
    return im2
    #im2.show()

def main():
    '''
    Fonction principale : charge une image et affiche son gradient
    '''
    # test data
    im = Image.open('originaux/3.jpg')
    #im = Image.open('Tour.png')
    gradient(im)
if __name__ == "__main__":
    main()