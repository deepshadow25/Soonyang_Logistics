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
        success, image = self.video.read()
    
        
        result = model.predict(source=image, save=True) 
        boxes = result[0].boxes

        if len(boxes) > 0 :
            flags = 0
            count = 0
            for i in range(len(boxes)):
                print(i+1,"번째 박스")
                box = boxes[i]  
                xmin = box.xyxy[0][0] 
                xmax = box.xyxy[0][2]
                xbox = (xmin+xmax)/2 
                if xbox>= 220 or xbox <= 420 and flags == 0:
                    print('중간')
                    flags = 1
                    count += 1
                    cv2.imread(f"./runs/detect/predict/image_{count}.jpg")
                if xbox >= 420 and flags == 1:
                    print('끝')
                    flags = 0
                
        dst = cv2.imread( "./runs/detect/predict2/image0.jpg")
        ret, jpeg = cv2.imencode('.jpg', image)
        
        return jpeg.tobytes()