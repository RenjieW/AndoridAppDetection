from PIL import Image
import math
import os
import time

start_time = time.time()
fileDir = "/Users/shaoyang/Desktop/smartphone/allRGB_malicious/"
fileDir2 = "/Users/shaoyang/Desktop/smartphone/allRGB_benign/"
outputDir2 = "/Users/shaoyang/Desktop/smartphone/img_benign/"
outputDir = "/Users/shaoyang/Desktop/smartphone/img_malicious/"

all_genome = os.listdir(fileDir)
all_benign = os.listdir(fileDir2)
for app in all_genome:
	if (str(app) == ".DS_Store"):
		continue
	app_name = str(app)[:40]
	print("Converting: " + str(app_name))
	f = open(fileDir + str(app), "r")
	line = f.readlines()[0].split("\t")
	X = int(math.ceil(math.sqrt(len(line))))
	Y = X
	index = 0
	image = Image.new("RGB", (X, Y))
	for x in range(0, X):
		for y in range(0, Y):
			if (len(line[index]) == 0):
				continue
			if (index > len(line)):
				image.putpixel((x, y), (0, 0, 0))
				continue
			rgb = line[index].split(",")
			image.putpixel((x, y), (int(rgb[0]), int(rgb[1]), int(rgb[2])))
			index += 1
	image.save(outputDir + app_name + ".jpg")
end_time_mal = time.time()
for app in all_benign:
	if (str(app) == ".DS_Store"):
		continue
	temp = str(app).index(".txt")
	app_name = str(app)[:temp]
	print("Converting: " + str(app_name))
	f = open(fileDir2 + str(app), "r")
	line = f.readlines()[0].split("\t")
	X = int(math.ceil(math.sqrt(len(line))))
	Y = X
	index = 0
	image = Image.new("RGB", (X, Y))
	for x in range(0, X):
		for y in range(0, Y):
			if (len(line[index]) == 0):
				continue
			if (index > len(line)):
				image.putpixel((x, y), (0, 0, 0))
				continue
			rgb = line[index].split(",")
			image.putpixel((x, y), (int(rgb[0]), int(rgb[1]), int(rgb[2])))
			index += 1
	image.save(outputDir2 + app_name + ".jpg")
end_time = time.time()
print("Converting malware time cost: " + str(end_time_mal - start_time) + "s")
print("Converting benign apps time cost: " + str(end_time - end_time_mal) + "s")