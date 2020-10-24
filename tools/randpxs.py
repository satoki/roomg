import cv2
import numpy
import random

h = int(input("h:"))
w = int(input("w:"))
s = int(input("seed:"))

print("o('p'o)")

random.seed(s)

image = numpy.zeros((h, w, 3))
for i in range(h):
    for j in range(w):
        for k in range(3):
            image[i][j][k] = random.randrange(256)

cv2.imwrite("image_{}.png".format(s), image)

print("OK")