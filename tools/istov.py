import os
import cv2
import sys

dirname = input("Directory Name:")
filename = dirname.replace("_images", "")

h = int(input("h:"))
w = int(input("w:"))
fps = float(input("fps:"))

video = cv2.VideoWriter("{}_istov.mp4".format(filename), cv2.VideoWriter_fourcc('m','p','4', 'v'), fps, (w, h))

n = 0

print("o('4'o)")

while os.path.exists("{}/{}_{}.png".format(dirname, filename, n)):
    image = cv2.imread("{}/{}_{}.png".format(dirname, filename, n))
    video.write(image)
    n += 1

video.release()

print("OK")