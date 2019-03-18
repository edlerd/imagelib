import cv2
import numpy as np

img = cv2.imread('grass.jpg')


def relight(img, diff):
    height, width, channels = img.shape

    for y in range(0, width):
        for x in range(0, height):
            for c in range(0, channels):
                img[x,y,c] = max(0, min(255, (img[x,y,c] + diff)))


def hist(img):
    height, width, channels = img.shape
    hist = np.zeros(256, np.uint32)

    for y in range(0, width):
        for x in range(0, height):
            hist[img[x,y]] += 1

    print(' '.join(str(e) for e in hist))


def histNorm(img):
    height, width, channels = img.shape
    hist = np.zeros(256, np.uint32)
    N = 0

    for y in range(0, width):
        for x in range(0, height):
            hist[img[x,y]] += 1
            N += 1

    histNorm = np.zeros(256, np.float64)
    for i in range(0, 256):
        histNorm[i] = hist[i] / N

    print(' '.join(str(e) for e in histNorm))


def histConvol(img):
    height, width, channels = img.shape
    hist = np.zeros(256, np.uint32)
    N = 0

    for y in range(0, width):
        for x in range(0, height):
            hist[img[x,y,0]] += 1
            N += 1

    histConvol = np.zeros(256, np.float64)
    for i in range(0, 256):
        histConvol[i] = hist[i] / N

    for i in range(1, 256):
        histConvol[i] += histConvol[i-1]

    print(' '.join(str(e) for e in histConvol))


def show(img):
    cv2.imshow('image',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def monochrome(img):
    height, width, channels = img.shape

    for y in range(0, width):
        for x in range(0, height):
            img[x,y] = 0.28*img[x,y,0] + 0.59*img[x,y,1] +0.13*img[x,y,2]
    

def foo():
    height, width, channels = img.shape
    
    r = np.zeros((height, width, 3), np.uint8)
    g = np.zeros((height, width, 3), np.uint8)
    b = np.zeros((height, width, 3), np.uint8)
    grey = np.zeros((height, width, 3), np.uint8)
    
    # kanäle aufsplitten
    for y in range(0, width):
        for x in range(0, height):
            r[x,y] = img[x,y,0]
            g[x,y] = img[x,y,1]
            b[x,y] = img[x,y,2]
            grey[x,y] = 0.25*img[x,y,0] + 0.5*img[x,y,1] +0.25*img[x,y,2]
    cv2.imwrite('r.jpg', r)
    cv2.imwrite('g.jpg', g)
    cv2.imwrite('b.jpg', b)
    cv2.imwrite('grey.jpg', grey)
    
    # cutoff image
    other = np.zeros((height, width, 1), np.uint8)
    for y in range(0, width):
        for x in range(0, height):
            other[x,y] = min(max(0.25*img[x,y,0] + 0.5*img[x,y,1] +0.25*img[x,y,2], 50), 200)
    cv2.imwrite('other.jpg', other)
