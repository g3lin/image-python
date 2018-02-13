from PIL import Image



def detect_seam(path_image_grad):
    im = Image.open(path_image_grad)
    seam = []
    y = im.size[1]-1 # On part du bas de l'image
    mincost = 999999999
    adress_x = 0
    

    # Calcul du cout pour la ligne du bas
    for x in range(0,im.size[0]):
        cost_pix = calculate_cost(0,im,x,y)
        if cost_pix < mincost:
            # On store le x pour lequel le cout est minimal
            adress_x = x 
    x = adress_x
    # On rajoute ce pixel avec le cout optimal au seam
    seam += [(x,y)]


    # Pour chaque ligne on fait le cout optimal de la ligne du dessus
    # On part de l'avant derniere ligne et on va à reculons jusqu'à -1 (non inclus)
    for y in range(im.size[1]-2,-1,-1):
        mincost = 999999999
        for x in range(x-1,x+2):
            cost_pix = calculate_cost(0,im,x,y)
            if cost_pix < mincost:
                # On store le x pour lequel le cout est minimal
                adress_x = x 
        x = adress_x

        # On rajoute ce pixel avec le cout optimal au seam
        seam += [(x,y)]

    return seam








def calculate_cost(cost,im, x, y):
     
    if y == 0:
        # si on est arrivé en haut de l'image retourner le coup
        return cost
    
    pix = im.load()
    #on ajoute la valeur du pixel courant au cout du seam
    cost += pix[x,y][1]

    if x-1 < 0:
        # cas où on est à gauche de l'image
        c2 = calculate_cost(cost,im,x,y-1)
        c3 = calculate_cost(cost,im,x+1,y-1)
        cost += min(c2,c3)

    elif x+1 >= im.size[0]:
        # cas où on est vers le milieu
        c1 = calculate_cost(cost,im,x-1,y-1)
        c2 = calculate_cost(cost,im,x,y-1)
        cost += min(c1,c2)

    else:
        # cas où on est vers la droite
        c1 = calculate_cost(cost,im,x-1,y-1)
        c2 = calculate_cost(cost,im,x,y-1)
        c3 = calculate_cost(cost,im,x+1,y-1)
        cost += min(c1,c2,c3)

    # permet de faire remonter le cout dans la récursion 
    return cost

    




def main():
    # test data
    detect_seam('/home/antoine/dev/data_images/1g.jpg')

if __name__ == "__main__":
    main()