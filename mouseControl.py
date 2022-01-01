import cv2
import handMediapipe as hm
import pyautogui as pg

width,height = pg.size()
cap = cv2.VideoCapture(0)

# w,h = pg.size()
# hm.change_res(cap,w,h)
# cv2.namedWindow('op', cv2.WND_PROP_FULLSCREEN)
# cv2.setWindowProperty('op', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
# _, img = cap.read()
pg.FAILSAFE = False
var = hm.handTrack(1,min_detection_confidence=0.8,min_tracking_confidence=0.6)
while 1:
    _, img = cap.read()
    img=cv2.flip(img, 1)
    img = var.findHands(img)

    # vw=img.shape[1]
    # vh=img.shape[0]
    # print(vw)
    # print(vh)    
    landmarks = var.getPosition(img)
    if landmarks:

        _,x,y = landmarks[8] # co ordinates of the index finger

        x,y = x*4,y*3 # changing the sacle to 1080p HD+

        # print(x,y)
        if x >width and y > height:
            pass 
        else:
            pg.moveTo(x,y)
        length = var.dis_btw_2points(8,12)
        if length<35:
            # if x >width and y > height:
            #     pass
            pg.click(x,y)
    
    cv2.imshow('op',img)

    if cv2.waitKey(1)==27:
        break


cap.release()
cv2.destroyAllWindows()

