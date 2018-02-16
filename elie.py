from PIL import Image

def main():

def remove_seam(im,seam):
    for x in range (im.size[0]):
        for elm in seam:
            if x > elm[0]:
                shift_left(im,1)
    return im

def shift_left(im,nombre):
    image = im.load()
    for x in range(im.size[0]):
        image[x,y]= image[x-nombre,y]

if __main__ == "__main__":
    main()