import cv2 
import numpy as np 

img = cv2.imread("./test.jpg")

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)

#contours, hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

contours=[]
ROI=[(100,100),(200,100),(200,200),(100,200)]
contours.append(np.array(ROI, np.int32))

cv2.drawContours(img,contours,-1,(0,0,255),3)


test_point=(110,110)
flag = cv2.pointPolygonTest(contours[0], test_point, False)
print(flag)

test_point=(300,300)
flag = cv2.pointPolygonTest(contours[0], test_point, False)
print(flag)

test_point=(110,100)
flag = cv2.pointPolygonTest(contours[0], test_point, False)
print(flag)

'''
print (type(contours))  
print (type(contours[0]))  
print (len(contours))  '''



#cv2.polylines(img, pts, True, (0, 0, 255), thickness=2)


cv2.imshow("img", img)
cv2.waitKey(0)

#flag = cv2.pointPolygonTest(contours[i], test_point, False)