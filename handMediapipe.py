import mediapipe as mp
import numpy as np
import cv2




def to1080p(cap):
    cap.set(3, 1920)
    cap.set(4, 1080)

def to720p(cap):
    cap.set(3, 1280)
    cap.set(4, 720)

def to480p(cap):
    cap.set(3, 640)
    cap.set(4, 480)

def change_res(cap,width, height):
    cap.set(3, width)
    cap.set(4, height)
    # cap.set(10,value) this changes the brightness 
    # of the output video

class handTrack:
    def __init__(self,maxHands=2,mode=False,
              min_detection_confidence=0.5, min_tracking_confidence=0.5,draw=True) -> None:
        '''
        maxHands : max number of hands to be detected 
        mode : static_image_mode set to FALSE by default which means 
            the solution provided by
            mediapipe treats input images as a video stream
        min_detection_confidence : the confidence threshold to detect 
            hands (by default set to 0.5 which is 50%)
        min_tracking_confidence : the confidence threshold for tracking the hands
            (set to 0.5 i.e. 50% by default), less than the threshold it will start 
            detecting for hands, when found it will track it
        draw : set to TRUE to draw the mediapipe hand landmarks
        '''
        
        self.maxHands = maxHands
        self.mode = mode
        self.mdc=min_detection_confidence
        self.mtc=min_tracking_confidence

        self.mpHands = mp.solutions.hands

        self.hands = self.mpHands.Hands(self.mode,self.maxHands,self.mdc,self.mtc)

        if draw:
            self.drawHands = mp.solutions.drawing_utils
        

    def  findHands(self,image):
        rgb_img = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(rgb_img)

        if self.results.multi_hand_landmarks:
            for landmarks in self.results.multi_hand_landmarks:
                self.drawHands.draw_landmarks(image,landmarks,
                        self.mpHands.HAND_CONNECTIONS)
        # return  cv2.flip(image, 1)
        return  image

    def getPosition(self,image, draw=False):

        self.landmarks_list =[]
        ''' 
        
        upon printing this will yield (id,x,y)
        id represents the hand landmarks number
        x,y being its respective coordinates '''
        # image=cv2.flip(image, 1)s

        if self.results.multi_hand_landmarks:
            
            hat = self.results.multi_hand_landmarks[0]
            for num,lm in enumerate(hat.landmark):
                h,w,c = image.shape 
                x,y = int(lm.x*w), int(lm.y*h) # to change the x,y into pixel dimensions [1280,720] 720p HD
                self.landmarks_list.append((num,x,y))
                if draw:
                    cv2.circle(image,(x,y), 15, (21,28,208),cv2.FILLED)
        return self.landmarks_list

    def dis_btw_2points(self,landmark1,landmark2):
        """
        landmark1 : 1st landmark number according to mediapipe
        landmark2 : 2nd landmark number according to mediapipe
        """
        _,x1,y1 = self.landmarks_list[landmark1] 
        _,x2,y2 = self.landmarks_list[landmark2] 
        distance = np.sqrt((x1-x2)**2 +(y1-y2)**2)
        return distance

        