# -*- coding: utf-8 -*-
from PIL import Image
import seam
import gradient_prewitt
import dual_gradient
import seam_treatment
import seam_carving
import agrandir

def main():

    im = Image.open('originaux/1.jpg')
    #image = im.load()
    img = dual_gradient.gradient(im)
    #print("grad fini")
    compteur = 100
    while compteur!=0:
        im, img = seam_carving.add_horizontal_carving(im,img)
        compteur-=1
        print(compteur)
    im.show()
    #img.show()
if __name__ == "__main__":
    main()