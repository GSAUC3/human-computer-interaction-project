import handMediapipe as hm 
import cv2,numpy as np
from collections import deque

cap = cv2.VideoCapture(0)
writingpad = np.zeros((460,640),np.uint8)
xprev,yprev =0,0
var = hm.handTrack(1)
while 1:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)

    a,landmarks,image = var.fingersUD(frame)
    if landmarks:
        _,x,y,_ = landmarks['index'][-1] # returns the coordinate of the tip of the index finger
        dq = deque()
        if a['index']==1 and a['middle']==0 and a['ring']==0:
            dq.append((x,y))
            if xprev==0 and yprev==0:
                xprev,yprev = x,y 
            cv2.line(image,(xprev,yprev),(x,y),(255,255,255),8)
            cv2.line(writingpad,(xprev,yprev),(x,y),(255,255,255),8)
            xprev,yprev = x,y 

        elif a['index']==1 and a['middle']==1 and a['ring']==0:
            # cv2.circle(writingpad,(x,y),8,(105,105,105),cv2.FILLED)
            xprev,yprev =0,0
        # elif a['index']==1 and a['middle']==1 and a['ring']==1 and a['pinky']==0:
        #     cv2.circle(writingpad,(x,y),18,(0,0,0),cv2.FILLED)
        elif a['index']==1 and a['middle']==1 and a['ring']==1 and a['pinky']==1 and a['thumb']==1:
            writingpad[:,:] = 0
            pass 
    # _,inv = cv2.threshold(writingpad,50,255,cv2.THRESH_BINARY_INV)
    # iinv = cv2.cvtColor(inv,cv2.COLOR_GRAY2BGR)
    # img = cv2.bitwise_and(image,iinv)
    # img = cv2.bitwise_or(img,writingpad)




    cv2.imshow('output',image)
    cv2.imshow('output2',writingpad)
    # cv2.imshow('output',image)
    # cv2.imshow('writing pad',writingpad)
    if cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()