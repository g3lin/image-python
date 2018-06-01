# -*- coding: utf-8 -*-
from PIL import Image
import math
def sobel(im):
    radius = 1
    im1 = im.load()
    im2 = Image.new('L', (im.size[0], im.size[1]))
    im3 = im2.load()
    Mx = [[-1,0,1],[-2,0,2],[-1,0,1]]
    My = [[-1,-2,-1],[0,0,0],[1,2,1]]
    for x in range(im.size[0]):
        for y in range(im.size[1]):
            Gxr, Gxg, Gxb = 0, 0, 0
            Gyr, Gyg, Gyb = 0, 0, 0
            for xp in range(x-radius, x+radius+1):
                if 0<=xp<im.size[0]:
                    for yp in range(y-radius, y+radius+1):
                        if 0<=yp<im.size[1]:
                            nx = xp-x+1
                            ny = yp-y+1
                            Gxr+= im1[xp, yp][0] * Mx[nx][ny]
                            Gyr+= im1[xp, yp][0] * My[nx][ny]
                            Gxg+= im1[xp, yp][1] * Mx[nx][ny]
                            Gyg+= im1[xp, yp][1] * My[nx][ny]
                            Gxb+= im1[xp, yp][2] * Mx[nx][ny]
                            Gyb+= im1[xp, yp][2] * My[nx][ny]
            G = round(math.sqrt(Gxr**2 + Gyr**2)+math.sqrt(Gxg**2 + Gyg**2)+math.sqrt(Gxb**2 + Gyb**2))
            im3[x,y] = G
    # return im2
    im2.show()

def main():
    # test data
    im = Image.open('originaux/1.jpg')
    sobel(im)
if __name__ == "__main__":
    main()