import handMediapipe as hm 
import cv2,numpy as np
from torch import nn 
import torch
from torchvision import transforms

# class Net(nn.Module):
#     def __init__(self):
#         super(Net,self).__init__()
        
#         self.conv1 = nn.Conv2d(1,6,3) # out 32
#         self.pool1 = nn.MaxPool2d(2,2) # out 16
#         self.conv2 = nn.Conv2d(6,16,3) # out 14
#         self.pool2 = nn.MaxPool2d(2,2) # out 7
#         self.conv3 = nn.Conv2d(16,26,3) # out 5
#         self.fc1 = nn.Linear(25*26,64)
#         self.fc2 = nn.Linear(64,26)
    
#     def forward(self,x):
#         x = nn.functional.relu(self.conv1(x))
#         x = self.pool1(x)
#         x = nn.functional.relu(self.conv2(x))
#         x = self.pool2(x)
#         x = nn.functional.relu(self.conv3(x))
#         x = x.view(-1,25*26)
#         x = self.fc1(x)
#         x = self.fc2(x)
#         # x1 = nn.functional.softmax(x)

#         return x 

# device = torch.device('cpu')
# model = Net()
# model.load_state_dict(torch.load('D:/Personal/tiyasa/codes/Review/src/Model.pth',map_location=device))

# def predict(model,x):
#     # x -> input frame
#     classes =['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
#      'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] 
#     model.eval()
#     transform = transforms.Compose([transforms.ToPILImage(),
#                                     transforms.ToTensor()])

#     x1 = torch.from_numpy(np.asarray(x))
#     x1 = x1.unsqueeze(0)
#     x1 = x1.unsqueeze(0)
#     out = model(x1)
#     print(classes[out.argmax(1).item()])

def convolution(image):
    kernel = np.zeros((160,160),dtype=np.uint8)
    kernel[2:-2,2:-2]=1
    ans = (kernel*image).sum()/25218
    np.set_printoptions(threshold=np.inf)
    if ans>10:
        return True
    return False


def draw_grid(image,size=80*2):
    
    for i in range(1,4):
        cv2.line(image,(i*size,0),(i*size,480-160),(255,255,255),1)
    for i in range(1,3):
        cv2.line(image,(0,i*size),(640,i*size),(255,255,255),1)
    return image

cap = cv2.VideoCapture(0)
writingpad = np.zeros((480,640,3),np.uint8)
xprev,yprev =0,0
var = hm.handTrack(1)
while 1:
    # i=0
    _, frame = cap.read()
    frame = cv2.flip(frame,1)

    a,landmarks,image = var.fingersUD(frame)
    if landmarks:
        _,x,y,_ = landmarks['index'][-1] # returns the coordinate of the tip of the index finger  
        if a['index']==1 and a['middle']==0 and a['ring']==0:
            
            if xprev==0 and yprev==0:
                xprev,yprev = x,y 
            cv2.line(image,(xprev,yprev),(x,y),(255,255,255),8)
            cv2.line(writingpad,(xprev,yprev),(x,y),(255,255,255),8)
            xprev,yprev = x,y 

        elif a['index']==1 and a['middle']==1 and a['ring']==0:
            xprev,yprev =0,0
        elif a['index']==1 and a['middle']==1 and a['ring']==1:
            # predict(model,writingpad)
            pad = cv2.cvtColor(writingpad,cv2.COLOR_BGR2GRAY)
            print(convolution(pad[:160,:160]))
            # print(convolution(pad[160:2*160,:160]))
            # print(convolution(pad[160*2:3*160,:160]))
            # print(convolution(pad[3*160:4*160,:160]))
            
        if a['index']==1 and a['middle']==1 and a['ring']==1 and a['pinky']==1 and a['thumb']==1:
            writingpad[:,:,:] = 0
            # print(writingpad.shape)

   


    # i+=1
    image = cv2.addWeighted(image,0.5,writingpad,0.6,0.0)
    image= draw_grid(image)
    cv2.imshow('output',image)
    # cv2.imshow('output2',writingpad)
    if cv2.waitKey(1)== ord('s'):
        cv2.imwrite('applePie.jpg',writingpad)
    elif cv2.waitKey(1)==27:
        break

cap.release()
cv2.destroyAllWindows()