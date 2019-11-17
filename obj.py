import cv2
import numpy as np





	

def ColRange():
#Define Red
    lower_red = np.array([161, 155, 84], dtype=np.uint8)

    upper_red = np.array([215, 255,255], dtype=np.uint8)
#    inRange(hsv, Scalar(0, 120, 70), Scalar(10, 255, 255), lower_red);
#    inRange(hsv, Scalar(170, 120, 70), Scalar(180, 255, 255), upper_red);

    red = [lower_red, upper_red, 'red']

    #Define Blue
    lower_blue = np.array([100, 150, 0], dtype=np.uint8)
    upper_blue = np.array([140, 255, 255], dtype=np.uint8)
    blue = [lower_blue, upper_blue, 'blue']
    
    #Define Yellow
    lower_yellow = np.array([5, 110, 200], dtype=np.uint8)
    upper_yellow = np.array([50, 255, 255], dtype=np.uint8)
    yellow = [lower_yellow, upper_yellow, 'yellow']
    
    #Define White
    lower_white = np.array([0, 90, 60], dtype=np.uint8)
    upper_white = np.array([10, 255, 255], dtype=np.uint8)    
    white = [lower_white, upper_white ,'white']
    
    #Define Green
    lower_green = np.array([40, 40, 40], dtype=np.uint8)
    upper_green = np.array([70, 250, 250], dtype=np.uint8)
    green = [lower_green, upper_green, 'green']

    colors=[blue,yellow,red,white,green]
    return colors

def Color(img):
     
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #lower_b=np.array([40,40,40])
    #upper_b=np.array([70,250,250])
    colors=ColRange()
    for color in colors:
        mask=cv2.inRange(hsv,color[0],color[1])
        res=cv2.bitwise_or(img,img,mask=mask)
    cv2.imshow('res',res)
    cv2.imwrite('changed2.png',res)
    cv2.waitKey(100)
    cv2.destroyAllWindows()
    



img=cv2.imread('shapes.png',1)
Color(img)

    





