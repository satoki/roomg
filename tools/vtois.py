import os
import cv2
import sys

args = sys.argv
filename = args[1]

video = cv2.VideoCapture(filename)
if not video.isOpened():
    print("plz {}".format(filename))
    sys.exit()

dirname = "{}_images".format(filename.replace(".mp4", ""))
os.makedirs(dirname, exist_ok=True)

n = 0

print("o('3'o)")

while True:
    ret, frame = video.read()
    if ret:
        cv2.imwrite("{}/{}_{}.png".format(dirname, filename.replace(".mp4", ""), n), frame)
        n += 1
    else:
        break

print("f:{}".format(n))

print("OK")