import cv2
import numpy as np
import handMediapipe as hm
import pyautogui as pg

width, height = pg.size()
cap = cv2.VideoCapture(0)
vw = 640
vh = 480
halfHeight = vh >> 1

# print(cv2.__version__)

cx = px = cy = py = 0
FACTOR = 30
ORIGIN = (80, 10)
SMOOTHIE = 2

pg.FAILSAFE = False
var = hm.handTrack(1)
while 1:
    _, img = cap.read()
    img = cv2.flip(img, 1)

    hm.frameRate(img)

    cv2.line(img, (0, halfHeight), (vw, halfHeight), (0, 255, 38), 1)
    cv2.line(img, (vw >> 1, 0), (vw >> 1, vh), (0, 255, 38), 1)

    a, landmarks, img = var.fingersUD(img)
    if landmarks:

        # print(a)

        _, x, y, z = landmarks['index'][3]

        _, x0, y0, z0 = landmarks['thumb'][3]

        # changing the sacle to 1080p HD+
        x = np.interp(x, (ORIGIN[0], ORIGIN[0]+16*FACTOR), (0, 1920))
        y = np.interp(y, (ORIGIN[0], ORIGIN[1]+9*FACTOR), (0, 1080))

        cx = px + (x-px)/SMOOTHIE
        cy = py + (y-py)/SMOOTHIE

        # horizontal line that will pass exactly through center of the screen

        # print(x,y,z)

        if a['index'] == 1:
            cv2.rectangle(
                img, ORIGIN, (ORIGIN[0]+16*FACTOR, ORIGIN[1]+9*FACTOR), (0, 255, 255), 4)
            if x < width and y < height:
                pg.moveTo(cx, cy)

            if a['thumb'] == 0 and a['middle'] == 1 and a['ring'] == 1:
                pg.scroll(-200)
            elif a['thumb'] == 0 and a['middle'] == 1 and a['ring'] == 0:
                pg.scroll(200)
            elif a['thumb'] == 1 and a['middle'] == 0 and a['ring'] == 1:
                pg.click(cx, cy)
            elif a['thumb'] == 1 and a['middle'] == 1 and a['ring'] == 0:
                pg.click(cx, cy, button='right')

            elif a['middle'] == 0 and a['ring'] == 0:
                pg.doubleClick()

            dis_tr = var.dis_btw_2points(4, 20)
            if dis_tr < 30:
                pg.mouseDown()
            else:
                pg.mouseUp()

            px, py = cx, cy

        if a['thumb'] == a['pinky'] == 1 and a['index'] == a['middle'] == a['ring'] == 0:
            pg.hotkey('win', 'tab')

    cv2.imshow('op', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
