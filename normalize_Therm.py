import os
import cv2
import glob
import numpy as np

def normalize(inputPath, savePath, normalizationMethod):
	# Set the save path if none was provided
	if savePath == "":
		savePath = os.path.join(inputPath, "Normalized_Images")

	# Ensure the save path exists
	if not os.path.exists(savePath):
		os.makedirs(savePath)

	# List all the images in the input path
	imgs_list = sorted(glob.glob(os.path.join(inputPath, "*.png")))
	print("Found %d images..." % len(imgs_list))

	# Process and normalize all the images
	index = 0
	for file in imgs_list:
		print("%d/%d" % (index, len(imgs_list)))

		img = cv2.imread(file, 0)
		if normalizationMethod == "hist":
			equ = cv2.equalizeHist(img)
		else:
			clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
			equ = clahe.apply(img)
		res = np.hstack((img, equ))
		#cv2.imshow("Image Comparison", res)
		#cv2.waitKey(0)
		cv2.imwrite(os.path.join(savePath, os.path.basename(file)), equ)

		index += 1



if __name__ == "__main__":
	inputFiles = ""
	saveDir = ""

	normalize(inputFiles, saveDir, "hist")