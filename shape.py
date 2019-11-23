import pytesseract
import numpy as np
import obj
import cv2
from PIL import Image

img = cv2.imread('testim3.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
colors=obj.ColRange()
kernel=np.ones((3,3),np.uint8)
mask1=cv2.inRange(hsv,colors[0][0],colors[0][1])
contours2,hierarchy2=cv2.findContours(mask1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for color in colors:
    mask=cv2.inRange(hsv,color[0],color[1])
    mask=cv2.erode(mask,kernel)
    if color[2]!="green":
    	flag=1    
    if((color[2]!="green" and flag==1) or (color[2]=="green" and flag==0)): 	
    	contours,hierarchy =cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
       
        
    
    if(len(contours)!=0):
        contours2=contours2+contours
        
    

    
   

c = max(contours2, key = cv2.contourArea)
x,y,w,h = cv2.boundingRect(c)
cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
approx = cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
if len(approx)==5:
    print ("pentagon")
    cv2.drawContours(img,c,0,255,-1)
elif len(approx)==3:
    print ("triangle")
    cv2.drawContours(img,c,0,(0,255,0),-1)
elif len(approx)==4:
    print ("square")
    cv2.drawContours(img,c,0,(0,0,255),-1)
elif len(approx) == 9:
    print ("half-circle")
    cv2.drawContours(img,c,0,(255,255,0),-1)
elif len(approx) > 15:
    print ("circle")
    cv2.drawContours(img,c,0,(0,255,255),-1)

crop=img[y:y+h, x:x+w]
cv2.imshow("cropped",crop)
tessdata_dir_config = '--tessdata-dir "/usr/local/Cellar/tesseract/4.1.0/share/tessdata" -l eng --psm 10 --oem 1'
arr = Image.fromarray(crop)
result = pytesseract.image_to_string(arr,lang='eng',config = tessdata_dir_config)
#cv2.drawContours(img,[c],0,(0,0,0),5)       
print(result)
cv2.imshow('img',img)
cv2.imwrite("changed2.png",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
