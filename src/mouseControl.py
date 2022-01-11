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

        _,x,y = landmarks[4] # co ordinates of the index finger (id,x,y)

        x,y = x*4,y*3 # changing the sacle to 1080p HD+
        
        

        janina = var.dis_btw_2points(4,17)
        print(janina)
        if janina > 108 and y <240:
            pg.press("pgup")
        if janina >108 and y>240:
            pg.press("pgdn")

        print(x,y)

        if a['index']==1:
            if x <width and y < height :
                pg.moveTo(x,y)
            length = var.dis_btw_2points(8,12)
            if length<35:
                if x <width and y < height:
                    pg.click(x,y)

                    
            len2 = var.dis_btw_2points(4,12)
            if len2<30:
                pg.press('enter')  
            

        elif a['middle']==1 and a['ring']==0:
            pg.press("pgdn")

        elif a['middle']==0 and a['ring']==1:
            pg.press("pgup")            
        

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

