# -*- coding: utf-8 -*-
from PIL import Image
import seam
import gradient_prewitt
import dual_gradient
import seam_treatment
import agrandir

def vertical_carving(im, img):
    cm = seam.calculate_cost_matrix(img)
    sm = seam.detect_seam(cm)
    #for elm in sm: #pour chaque element du seam (de la forme (x,y))
        #   im.load()[elm[0],elm[1]]= 255, 0, 0
    #im.show()
    im = seam_treatment.remove_seam(im,sm)
    img = seam_treatment.remove_seam(img,sm)
    return (im, img)

def horizontal_carving(im,img):
    im = im.rotate(-90, expand=True)
    img = img.rotate(-90, expand=True)
    im, img = vertical_carving(im,img)
    im = im.rotate(90, expand=True)
    img = img.rotate(90, expand=True)
    return (im, img)

def add_horizontal_carving(im, img):
    cm = seam.calculate_cost_matrix(img)
    sm = seam.detect_seam(cm)
    #for elm in sm: #pour chaque element du seam (de la forme (x,y))
        #   im.load()[elm[0],elm[1]]= 255, 0, 0
    #im.show()
    im = agrandir.add_seam_image(im,sm)
    img = agrandir.add_seam_gradient(img,sm)
    return (im, img)

def add_vertical_carving(im, img):
    im = im.rotate(-90, expand=True)
    img = img.rotate(-90, expand=True)
    im, img = add_horizontal_carving(im, img)
    im = im.rotate(90, expand=True)
    img = img.rotate(90, expand=True)
    return (im, img)

if __name__ == "__main__":
    vertical_carving(Image.open('1.jpg'), Image.open('1g.jpg'))