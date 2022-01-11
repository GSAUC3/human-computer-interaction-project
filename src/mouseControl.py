import cv2, numpy as np
import handMediapipe as hm
import pyautogui as pg

width,height = pg.size()
cap = cv2.VideoCapture(0)

pg.FAILSAFE = False
var = hm.handTrack(1)
while 1:
    _, img = cap.read()
    img=cv2.flip(img, 1)
    img = var.findHands(img)

    hm.frameRate(img)
    # vw=img.shape[1]
    # vh=img.shape[0]
    # print(vw)
    # print(vh)    
    landmarks = var.getPosition(img)
    a= var.fingersUD()
    if landmarks:

        _,x,y = landmarks[8] # co ordinates of the index finger (id,x,y)

        x,y = x*4,y*3 # changing the sacle to 1080p HD+
        
        


        print(x,y)

        if a['index']==1:
            if x <width and y < height :
                pg.moveTo(x,y)
            length = var.dis_btw_2points(8,12)
            if length<35:
                if x <width and y < height:
                    pg.click(x,y)

                    
            len2 = var.dis_btw_2points(4,8)
            if len2<30:
                pg.press('enter')  
            
        if a['index']==a['thumb']==a['middle']==a['ring']==a['pinky']==0:
            pg.keyDown('alt')
            pg.press('tab',interval=1)
        else:
            pg.keyUp('alt')

        
    cv2.imshow('op',img)


    if cv2.waitKey(1)==27:
        break


cap.release()
cv2.destroyAllWindows()

