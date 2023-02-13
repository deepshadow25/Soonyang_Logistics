import cv2
import torch
import numpy as np
from ultralytics import YOLO
from PIL import Image

model = YOLO("result/order_number.pt")

class OCRDetect(object):
    
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, frame = self.video.read()
        
        result = model.predict(source=frame, save=True)

        boxes = result[0].boxes
        
        if len(boxes) > 0 :
            flags = 0
            count = 0
            for i in range(len(boxes)):
                print(i+1,"번째 박스")
                box = boxes[i]
                x1 = box.xyxy[0][0]
                y1 = box.xyxy[0][1]
                x2 = box.xyxy[0][2]
                y2 = box.xyxy[0][3]
                x1 = x1.item()
                y1 = y1.item()
                x2 = x2.item()
                y2 = y2.item()
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)
                print(x1,y1,x2,y2,type(x1))
                
                xbox = (x1+x2)/2   
                if xbox>= 220 and xbox <= 420 and flags == 0:
                    print('중간')
                    flags = 1
                    count += 1
                    img = cv2.imread("runs\detect\predict\image0.jpg")
                    
                    path = "ocr_result\cropimage.jpg"
                    img = img[y1:y2, x1:x2]
                    cv2.imwrite(path,img)

                if xbox >= 540 and flags == 1:
                    print('끝')
                    flags = 0 
                    
        dst = cv2.imread( "runs\detect\predict\image0.jpg")
        ret, jpeg = cv2.imencode('.jpg', frame)
        
        return jpeg.tobytes()