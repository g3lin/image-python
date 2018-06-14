# -*- coding: utf-8 -*-
from PIL import Image

def add_seam_image(im,seam):
    '''
    
    '''
    image = im.load()
    im2 = Image.new('RGB', (im.size[0]+1, im.size[1]))
    image2 = im2.load()
    for elm in seam:
        #print (elm)
        for x in range(elm[0]+1):
            image2[x, elm[1]] = image[x,elm[1]]
        if (elm[0] == (im.size[0]-1)):
            r1, g1, b1 = image[elm[0], elm[1]]
            r2, g2, b2 = image[elm[0]-1, elm[1]]
            image2[elm[0]+1, elm[1]] = (r1+r2)//2, (g1+g2)//2, (b1+b2)//2
        else:
            r1, g1, b1 = image[elm[0], elm[1]]
            r2, g2, b2 = image[elm[0]+1, elm[1]]
            image2[elm[0]+1, elm[1]] = (r1+r2)//2, (g1+g2)//2, (b1+b2)//2
            for x in range(elm[0]+1, im.size[0]):
                image2[x+1, elm[1]] = image[x, elm[1]]
    return  im2 #l'image modifiée est retournée

def add_seam_gradient(im,seam):
    '''
    
    '''
    image = im.load()
    im2 = Image.new('L', (im.size[0]+1, im.size[1]))
    image2 = im2.load()
    for elm in seam:
        for x in range(elm[0]):
            image2[x, elm[1]] = image[x,elm[1]]
        image2[elm[0], elm[1]] = 255
        if (elm[0] == (im.size[0]-1)):
            x1 = image[elm[0], elm[1]]
            x2 = image[elm[0]-1, elm[1]]
            image2[elm[0]+1, elm[1]] = ((x1+x2)//2, )
        else:
            x1 = image[elm[0], elm[1]]
            x2 = image[elm[0]+1, elm[1]]
            image2[elm[0]+1, elm[1]] = ((x1+x2)//2, )
            for x in range(elm[0]+1, im.size[0]):
                image2[x+1, elm[1]] = image[x, elm[1]]
    return  im2 #l'image modifiée est retournée
