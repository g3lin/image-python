# -*- coding: utf-8 -*-
'''
Troisième étape : Destruction de la seam déterminée et décalage de l'image


A ce stade, on dispose de : 
    - une image à traiter
    - (Anthony) sa carte d'énergie
    - (Antoine) une fonction calculate_cost_matrix qui détermine une matrice des coûts de l'image
    - (Antoine) une fonction detect_seam utilisant la matrice de coûts, et qui retourne la seam verticale
        à enlever sous forme de tuple de coordonnées

Ce fichier permet de supprimer la seam calculée en deux étapes : 
    - Destruction de la seam en décalant les pixels par dessus
    - Redimensionnement de l'image
'''

from PIL import Image
import seam
import gradient_prewitt
import dual_gradient

def remove_seam(im,seam):
    '''
    Cette fonction décale tous les pixels à droite du seam par dessus, la
    redimensionne et la retourne 
    '''
    image = im.load()
    for elm in seam: #pour chaque element du seam (de la forme (x,y))
        for x in range (elm[0],im.size[0]-1): #pour chaque x 
            image[x,elm[1]] = image[x+1,elm[1]]
    #final =  resize(im,(im.size[0]-1,im.size[1]))
    box = (0,0,im.size[0]-1,im.size[1])
    im2 = im.crop(box)    
    return  im2 #l'image modifiée est retournée
