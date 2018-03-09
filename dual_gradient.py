from PIL import Image
import math
def gradient(im):
    im1 = im.load()
    im2 = Image.new('L', (im.size[0], im.size[1]))
    im3 = im2.load()
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            xpl = (x-1)%im.size[0]
            xpr = (x+1)%im.size[0]
            ypu = (y-1)%im.size[1]
            ypd = (y+1)%im.size[1]
            drx = im1[xpl, y][0] - im1[xpr, y][0]
            dgx = im1[xpl, y][1] - im1[xpr, y][1]
            dbx = im1[xpl, y][2] - im1[xpr, y][2]
            dry = im1[x, ypu][0] - im1[x, ypd][0]
            dgy = im1[x, ypu][1] - im1[x, ypd][1]
            dby = im1[x, ypu][2] - im1[x, ypd][2]
            G = round(math.sqrt(drx**2+dgx**2+dbx**2+dry**2+dgy**2+dby**2))
            im3[x,y] = G
    # return im2
    im2.show()

def main():
    # test data
    im = Image.open('originaux/3.jpg')
    #im = Image.open('Tour.png')
    gradient(im)
if __name__ == "__main__":
    main()