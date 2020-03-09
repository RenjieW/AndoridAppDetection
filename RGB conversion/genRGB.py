import sys
import os
import time

start_time = time.time()
resourcesDir = "/Users/shaoyang/Desktop/smartphone/resource_malicious/"
resources = os.listdir(resourcesDir)
for app in resources:
	dex = "/Users/shaoyang/Desktop/smartphone/resource_malicious/" + str(app) + "/classes.dex"
	if (str(app) == ".DS_Store"):
		continue
	if (not os.path.isfile(dex)):
		continue
	print("Converting: " + str(app))
	data = list()
	RGBfile = "/Users/shaoyang/Desktop/smartphone/allRGB_malicious/" + str(app) + ".txt"
	with open(dex, "rb") as f:
		source = f.read()
	source = source.encode("hex")
 
	while (len(source) > 0):
		temp = source[:6]
		data.append(temp)
		source = source[6:]
	f = open(RGBfile, "w")
	for i in data:
		if (len(i) == 6):
			r_bin = i[:2]
			g_bin = i[2:4]
			b_bin = i[4:]
			R = int(r_bin, 16)
			G = int(g_bin, 16)
			B = int(b_bin, 16)
			RGB = str(R) + "," + str(G) + "," + str(B)
			f.write(str(RGB) + "\t")
			continue
		if (len(i) == 4):
			r_bin = i[:2]
			g_bin = i[2:4]
			b_bin = "0"
			R = int(r_bin, 16)
			G = int(g_bin, 16)
			B = int(b_bin, 16)
			RGB = str(R) + "," + str(G) + "," + str(B)
			f.write(str(RGB) + "\t")
			continue
		if (len(i) == 2):
			r_bin = i[:2]
			g_bin = "0"
			b_bin = "0"
			R = int(r_bin, 16)
			G = int(g_bin, 16)
			B = int(b_bin, 16)
			RGB = str(R) + "," + str(G) + "," + str(B)
			f.write(str(RGB) + "\t")
			continue
	f.close()
end_time = time.time()
total_time = end_time - start_time
print("Total time spent: " + str(total_time))
