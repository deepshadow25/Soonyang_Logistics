import cv2
import torch
import numpy as np
from ultralytics import YOLO
from PIL import Image

model = YOLO("result/yolov8n.pt")
#model = torch.load('../result/yolov5s.pt')
#model.eval()
#model = torch.hub.load('./yolov5', 'custom','./result/yolov5l_best.pt', source='local')

class VideoCamera(object):
    
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture(0)
        # self.video = cv2.resize(self.video,(840,640))
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        #image=cv2.flip(image, -1)
        #print(image.shape)
        #results = model(image)
        #a = np.squeeze(results.render())

        '''
        count = 0
        while success:
            success, image = self.video.read()
            #if count % 10 ==0:
            if count % 3 ==0:
                res = model(image)
                res = list(res)[0]
                print(res.boxes.xyxyn)
                print(res.masks)
                #cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file
                #print("result",results.pandas().xyxy[0])
                #print('Read a new frame: ', success)
            count += 1
        '''        

        # We are using Motion JPEG, but OpenCV defaults to capture raw images,
        # so we must encode it into JPEG in order to correctly display the
        # video stream.
        
        result = model.predict(source=image, save=True) #욜로는 default로 /runs/detect/predict에 저장함
        """
        #print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        boxes = result[0].boxes
        #print(boxes)
        #print("======================================")
        if len(boxes) > 0 :
            flags = 0
            count = 0
            for i in range(len(boxes)):
                print(i+1,"번째 박스")
                box = boxes[i]  # returns one box
                #print(box.xyxy[0]) # 하나의 박스의 xyxy
                xmin = box.xyxy[0][0] # xmin값
                xmax = box.xyxy[0][2]
                # print(box.cls) # 클래스값
                xbox = (xmin+xmax)/2   # x 중심좌표
                if xbox>= 220 or xbox <= 420 and flags == 0:
                    print('중간')
                    flags = 1
                    count += 1
                    cv2.imread(f"./runs/detect/predict/image_{count}.jpg")
                if xbox >= 420 and flags == 1:
                    print('끝')
                    flags = 0
                

        #print(type(result[0].xyxy))
        #print(dir(result[0].numpy()))

        
        #if len(result[0].numpy()) > 1:
        #    print("@@@@@@@@@@@@",list(result[0].numpy())[1])
 
        #if len(result[0].cpu().numpy()) != 0:
            #print('데이터타입',result[0].cpu().numpy())
            #flag = False
            #count = 0
            #result[0].cpu().numpy()[0]
            #for i in result[0].cpu().numpy():
            #    print(i, type(i))
                #xmin = result[0].cpu().numpy()[i][0]
                #xmax = result[0].cpu().numpy()[i][2]
                #print(xmin, xmax)
                #xbox = (xmin + xmax) / 2
                #if xbox >= 420 or xbox <= 540:
                #    print('중간')
                #    cv2.imread( "./runs/detect/predict/image%d.jpg" % count)
                #    flag = True
                #if xbox >= 900 and flag==True:
                 #   print('끝')
                 #   flag = False
        #print(result.tensor.list)
        #dst = cv2.imread( "./runs/detect/predict/image0.jpg")
        """
        ret, jpeg = cv2.imencode('.jpg', image)
        
        return jpeg.tobytes()