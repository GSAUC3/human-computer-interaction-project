import cv2 
import numpy as np

def draw_grid(image,size=80*2):
    
    for i in range(1,4):
        cv2.line(image,(i*size,0),(i*size,480),(255,255,255),1)
    for i in range(1,3):
        cv2.line(image,(0,i*size),(640,i*size),(255,255,255),1)
    return image

img = cv2.imread('./applePie.jpg')
print(img.shape)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

flag,thresh = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
img2, contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print(img2)
start_point = [292, 193]
end_point=[338, 258]

print([np.amax(i) for i in img2])
print([np.amin(i) for i in img2])
img = cv2.rectangle(img, start_point, end_point,(0,255,0),2)
img = draw_grid(img)
cv2.drawContours(img,img2,-1,(0,255,0),3)
cv2.imshow('contours',img)
cv2.waitKey(0)


