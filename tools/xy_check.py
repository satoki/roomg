import cv2
import sys
import numpy

args = sys.argv
filename = args[1]

video = cv2.VideoCapture(filename)
if not video.isOpened():
    print("plz {}".format(filename))
    sys.exit()

h = int(input("h:")) - 1
w = int(input("w:")) - 1

f = 0
image = []

while True:
    ret, color = video.read()
    if not ret:
        break
    f += 1
    image.append(color[h][w])

image = numpy.array([image] * 20)

print("f:{}".format(f))

cv2.imwrite('{}_{}_{}_check.png'.format(filename.replace(".mp4", ""), h + 1, w + 1), image)
print("OK")