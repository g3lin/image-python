from PIL import Image



def calculate_cost_matrix(path_image_grad):
    im = Image.open(path_image_grad)
    cost_matrix = []    
    pix = im.load()

    # Calcul de la matrice des couts
    for y in range(0,im.size[1]):
        tabline = []

        for x in range(0, im.size[0]):
            cost = pix[x,y][0]
            if y>0:
                if x-1 < 0:
                    # cas où on est à gauche de l'image
                    c2 = cost_matrix[len(cost_matrix)-1][x]
                    c3 = cost_matrix[len(cost_matrix)-1][x+1]
                    cost = pix[x,y][0] + min(c2,c3)


                elif x+1 >= im.size[0]:
                    # cas où on est vers le milieu
                    c1 = cost_matrix[len(cost_matrix)-1][x-1]
                    c2 = cost_matrix[len(cost_matrix)-1][x]
                    cost = pix[x,y][0] + min(c1,c2)

                else:
                    # cas où on est vers la droite
                    c1 = cost_matrix[len(cost_matrix)-1][x-1]
                    c2 = cost_matrix[len(cost_matrix)-1][x]
                    c3 = cost_matrix[len(cost_matrix)-1][x+1]
                    cost = pix[x,y][0] + min(c1,c2,c3)
            tabline += [cost]


        cost_matrix += [tabline]    
    
    return cost_matrix

def detect_seam(cost_matrix):
    seam = []
    y = len(cost_matrix)-1
    min_x_value = cost_matrix[y][0]
    min_x = 0
    for x in range( len(cost_matrix[1])-1 ):
        if cost_matrix[y][x] < min_x_value:
            min_x_value = cost_matrix[y][x]
            min_x = x
    x = min_x
    seam += [(x,y)]


    for y in range(len(cost_matrix)-2, -1,-1):
        min_x_value = cost_matrix[y][x]
        min_x = x
        for x in range( x-1,x+2 ):
            if cost_matrix[y][x] < min_x_value :
                min_x_value = cost_matrix[y][x]
                min_x = x
        x = min_x
        seam += [(x,y)]

    return seam


def main():
    # test data
    cm = calculate_cost_matrix('/home/antoine/dev/data_images/1g.jpg')
    sm = detect_seam(cm)


if __name__ == "__main__":
    main()