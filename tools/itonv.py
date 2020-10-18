import cv2
import sys
import copy
import random

filename = sys.argv[1]

frame = int(input("frame:"))
fps = float(input("fps:"))

image = cv2.imread(filename)
h = len(image)
w = len(image[0])

randlist = []
for i in range(h):
    for j in range(w):
        randlist.append((i,j))

random.shuffle(randlist)

video = cv2.VideoWriter("itonv_{}_{}.mp4".format(filename.replace(".png",""), fps), cv2.VideoWriter_fourcc('m','p','4', 'v'), fps, (w, h))

print("o('4'o)")

##############################
probability = 100000
##############################

count = 0
frame_c = 0
pixels = h * w #len(randlist)
image1 = copy.deepcopy(image)
while True:
    if count >= pixels - 1:
        random.shuffle(randlist)
        count = 0
    if not random.randrange(probability):
        if frame_c >= frame:
            break
        video.write(image1)
        frame_c += 1
        print(frame_c)
        image1 = copy.deepcopy(image)
        ##############################
        no_noises_frames = 5
        ##############################
        if frame_c + no_noises_frames>= frame:
            no_noises_frames = frame - frame_c
        for i in range(no_noises_frames):
            video.write(image)
            frame_c += 1
            print(frame_c)
    else:
        for i in range(3):
            image1[randlist[count][0]][randlist[count][1]][i] = random.randrange(255)
        count += 1

video.release()

print("OK")