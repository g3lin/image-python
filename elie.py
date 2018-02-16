from PIL import Image

def main():
    cm = calculate_cost_matrix('/home/antoine/dev/data_images/1g.jpg')
    sm = detect_seam(cm)
    image_smc = remove_seam('/home/antoine/dev/data_images/1.jpg')

def remove_seam(im,seam):
    for elm in seam: #pour chaque element du seam
        for x in range (im.size[0]): #pour chaque x 
            for y in range (im.size[1]):# pour chaque y
                if x > elm[0] and y == elm[1]: #lorsque x est supérieur à l'élement 0 et y vaut l'élement 1
                    shift_left(im,1) # on decale les pixels de 1 vers la gauche => "supprime" le pixel de coordonnée (x,y)
    return im #l'image modifiée est retournée

def shift_left(im,nombre):
    image = im.load() # on charge l'image pour pouvoir la modifier
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            image[x,y]= image[x-nombre,y] # decalage des pixels a gauche

if __name__ == "__name__":
    main()