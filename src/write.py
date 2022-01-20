import handMediapipe as hm
import cv2,numpy as np
from collections import deque

xp=yp=0

cap = cv2.VideoCapture(0)
drawingScreen = np.zeros((480,640,3),np.uint8)

drawingScreen[:,:,0]=255
drawingScreen[:,:,1]=255
drawingScreen[:,:,2]=255
var = hm.handTrack(1)

while 1:
    _,image = cap.read()
    image = cv2.flip(image,1)

    # hm.frameRate(image)
    a,landmarks,image = var.fingersUD(image)

    if landmarks:
        _,x,y,_ = landmarks['index'][-1]

        if a['index']==1 and a['middle']==0:
            #cv2.circle(drawingScreen,(x,y),10,(0,255,0),cv2.FILLED)    
            if xp==yp==0:
                xp,yp=x,y
            # cv2.line(image,(xp,yp),(x,y),(0,255,0),5)
            cv2.line(drawingScreen,(xp,yp),(x,y),(0,0,0),5)
            xp,yp=x,y

        elif a['index']==1 and a['middle']==1 and a['ring']==1:
            # cv2.circle(image,(x,y),10,(0,255,0),cv2.FILLED)    
            if xp==yp==0:
                xp,yp=x,y
  
            cv2.line(drawingScreen,(xp,yp),(x,y),(255,255,255),69)
            xp,yp=x,y

        
    cv2.imshow('output',image)
    cv2.imshow('draw',drawingScreen)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()