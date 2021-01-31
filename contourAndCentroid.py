#utf-8
#code by https://github.com/hahahihidede/




import cv2
import numpy as np


img = cv2.imread('./initialStateImages/Caucasus.png') #image Source, set as the same as your image path

image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Convert image to grayscale

contours, _ = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #look for contours

print("no of shapes: {0}".format(len(contours))) 

for cnt in contours:
	rect = cv2.minAreaRect(cnt)
	box = cv2.boxPoints(rect)
	box = np.int0(box)
	img = cv2.drawContours(img, [box], 0, (0,0,255)) #BGR_Color_Sequence
#===================================================================

#look for center of your images ===========================
for cnt in contours:
	M = cv2.moments(cnt)
	cx = int(M['m10']/M['m00'])
	cy = int(M['m01']/M['m00'])
	center = (cx, cy)
	print("Center coordinate: "+str(center))
	radius = 5
	cv2.circle(img, (cx,cy), radius, (0, 255, 255), -1)
#===================================================================

#put polygn on your images ==========================================
	epsilon = 0.01*cv2.arcLength(cnt, True)
	approx = cv2.approxPolyDP(cnt, epsilon, True)
	img = cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
#===================================================================

cv2.imshow('ImageWindow', img) #Show your final image
cv2.waitKey(0)








#visit my linkedin for more information about me https://www.linkedin.com/in/dederohmat/
