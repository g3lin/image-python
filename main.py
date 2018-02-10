from PIL import Image



def detect_seam(path_image_grad):
    im = Image.open(path_image_grad)
    seam = []
    y = im.size[1]
    mincost = 256
    adress_x = 0
    
    for x in range(0,im.size[0]):
        cost_pix = calculate_cost(0,im,x,y)
        if cost_pix < mincost:
            adress_x = x 
    x = adress_x
    seam += [(x,y)]

    for y in range(im.size[1]-2,0,-1):
        x = adress_x
        mincost = 256
        for x in range(x-1,x+2):
            cost_pix = calculate_cost(0,im,x,y)
            if cost_pix < mincost:
                adress_x = x 
        x = adress_x
        seam += [(x,y)]

    return seam








def calculate_cost(cost,im, x, y):
    if y == 0:
        return cost
    
    pix = im.load()
    cost += pix[x,y]
    if x-1 > 0:
        c1 = calculate_cost(cost,im,x-1,y-1)
    c2 = calculate_cost(cost,im,x,y-1)
    if x+1 < im.size[0]:
        c3 = calculate_cost(cost,im,x+1,y-1)

    cost += min(c1,c2,c3)


    




def main():
    detect_seam('/home/antoine/dev/data_images/1g.jpg')

if __name__ == "__main__":
    main()