import cv2
import numpy as np



def green(img):
     
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_b=np.array([40,40,40])
    upper_b=np.array([70,250,250])
    mask=cv2.inRange(hsv,lower_b,upper_b)
    
    res=cv2.bitwise_and(img,img,mask=mask)
    cv2.imshow('res',res)
    cv2.imwrite('changed.png',res)
    cv2.waitKey(100)
    cv2.destroyAllWindows()
    

def main():
	#print(cv2.__version__)

	img=cv2.imread('objy.png',1)
	#print(img)
	cv2.imshow('image',img)
	green(img)
	main()




