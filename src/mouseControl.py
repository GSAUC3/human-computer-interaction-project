import cv2, numpy as np
import handMediapipe as hm
import pyautogui as pg

width,height = pg.size()
cap = cv2.VideoCapture(0)
vw=640
vh=480
halfHeight = vh>>1

# print(cv2.__version__)

cx=px=cy=py=0
FACTOR = 30
ORIGIN = (80,10)
SMOOTHIE = 1.75

pg.FAILSAFE = False
var = hm.handTrack(1)
while 1:
    _, img = cap.read()
    img=cv2.flip(img, 1)
    img = var.findHands(img)

    hm.frameRate(img)
        
    cv2.line(img,(0,halfHeight),(vw,halfHeight),(0, 255, 38),1)
    cv2.line(img,(vw>>1,0),(vw>>1,vh),(0, 255, 38),1)

    a,landmarks = var.fingersUD(img)
    if landmarks:

        # print(a)

        _,x,y = landmarks['index'][-1]

        _,x0,y0 = landmarks['thumb'][-1]

        # changing the sacle to 1080p HD+
        x= np.interp(x,(ORIGIN[0],ORIGIN[0]+16*FACTOR),(0,1920))
        y= np.interp(y,(ORIGIN[0],ORIGIN[1]+9*FACTOR),(0,1080))

        cx = px + (x-px)/SMOOTHIE
        cy = py + (y-py)/SMOOTHIE

        # horizontal line that will pass exactly through center of the screen

        # print(x,y)

        if a['index']==1:
            cv2.rectangle(img,ORIGIN,(ORIGIN[0]+16*FACTOR,ORIGIN[1]+9*FACTOR),(0,255,255),4)
            if x <width and y < height :
                pg.moveTo(cx,cy)
            length = var.dis_btw_2points(8,12)
            if length<35:
                if x <width and y < height:
                    pg.click(cx,cy)

            px,py = cx, cy           
        #     len2 = var.dis_btw_2points(4,12)
        #     if len2<30:
        #         pg.press('enter')  
            
        

        elif a['index']==a['thumb']==a['middle']==a['ring']==a['pinky']==0:
            # pg.keyDown('alt')
            # pg.press('tab',interval=1)
            pg.hotkey('win','tab')
        

        if a['middle']==1 and a['ring']==0:
            pg.press("pgdn")

        if a['middle']==0 and a['ring']==1:
            pg.press("pgup")            

        dis0 = var.dis_btw_2points(4,17)
        if dis0 > 108 and y0 <halfHeight:
            pg.press("pgup")
        if dis0 >108 and y0>halfHeight:
            pg.press("pgdn")
        
    cv2.imshow('op',img)


    if cv2.waitKey(1)==27:
        break


cap.release()
cv2.destroyAllWindows()

