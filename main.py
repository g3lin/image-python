from PIL import Image
import seam
import gradient_prewitt
import dual_gradient
import seam_treatment
import seam_carving

def main():
    '''
    Fonction principale : charge une image et son gradient et applique
    un seam carving k fois en plusieurs étapes ... : 
        - Calcul d'une matrice de coût de l'image à partir de son gradient
        - Detection de la seam optimale à partir de la pmatrice de coût
        - Suppression de la seam déterminée
    en affichant l'image à chaque fin de boucle pour suivre l'évolution
    '''
    im = Image.open('1.jpg')
    #image = im.load()
    img = dual_gradient.gradient(im)
    print("grad fini")
    compteur = 10
    while compteur!=0:
        im, img = seam_carving.horizontal_carving(im,img)
        compteur-=1
    im.show()
    #img.show()
if __name__ == "__main__":
    main()