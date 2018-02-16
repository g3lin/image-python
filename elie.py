from PIL import Image
import seam
import gradient_prewitt

def remove_seam(im,seam):
    for elm in seam: #pour chaque element du seam
        for x in range (im.size[0]): #pour chaque x 
            for y in range (im.size[1]):# pour chaque y
                if x > elm[0] and y == elm[1]: #lorsque x est supérieur à l'élement 0 et y vaut l'élement 1
                    image = shift_left(im,1) # on decale les pixels de 1 vers la gauche => "supprime" le pixel de coordonnée (x,y)
    return image #l'image modifiée est retournée

def shift_left(im,nombre):
    image = im.load() # on charge l'image pour pouvoir la modifier
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            image[x,y]= image[x-nombre,y] # decalage des pixels a gauche
    return im

def main():
    im = Image.open('Images_test_python/originaux/1.png')
    img = gradient_prewitt.prewitt(im)
    cm = seam.calculate_cost_matrix(img)
    sm = seam.detect_seam(cm)
    image_smc = remove_seam(im,sm)
    image_smc.show()

if __name__ == "__main__":
    main()