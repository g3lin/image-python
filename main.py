from PIL import Image



def calculate_cost_matrix(path_image_grad):
    im = Image.open(path_image_grad)
    cost_matrix = []    
    pix = im.load()

    # Calcul de la matrice des couts
    for y in range(0,im.size[1]):
        tabline = []

        for x in range(0, im.size[0]):
            cost = pix[x,y]
            if y>0:
                if x-1 < 0:
                    # cas où on est à gauche de l'image
                    c2 = pix[x,y-1]
                    c3 = pix[x+1,y-1]
                    cost = pix[x,y] + min(c2,c3)


                elif x+1 >= im.size[0]:
                    # cas où on est vers le milieu
                    c1 = pix[x-1,y-1]
                    c2 = pix[x,y-1]
                    cost = pix[x,y] + min(c1,c2)

                else:
                    # cas où on est vers la droite
                    c1 = pix[x-1,y-1]
                    c2 = pix[x,y-1]
                    c3 = pix[x+1,y-1]
                    cost = pix[x,y] + min(c1,c2,c3)
            tabline += [cost]


        cost_matrix += [tabline]    
    
    return cost_matrix






def main():
    # test data
    calculate_cost_matrix('/home/antoine/dev/data_images/1g.jpg')

if __name__ == "__main__":
    main()