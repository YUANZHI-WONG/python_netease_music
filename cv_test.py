import cv2 
import numpy as np
#手动添加区域点
contours=[]
ROI=[(100,100),(200,100),(200,200),(100,200)]
contours.append(np.array(ROI, np.int32))


'''
判断点是否在多边形内
'''
test_point=(110,110)
flag = cv2.pointPolygonTest(contours[0], test_point, False)
print(flag)
