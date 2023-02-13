import cv2
import torch
import numpy as np
from ultralytics import YOLO
from PIL import Image

model = YOLO("result/yolov8n.pt")

class VideoCamera(object):
    count = 0

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
            print(VideoCamera.count)
            print('카운트--------')
            for i in range(len(boxes)):
                print(i+1,"번째 박스")
                box = boxes[i]  
                xmin = box.xyxy[0][0] # xmin값
                xmax = box.xyxy[0][2] # xmax값
                xbox = (xmin+xmax)/2   # x 중심좌표
                if xbox>= 220 and xbox <= 420 and flags == 0:
                    print('중간')
                    flags = 1
                    VideoCamera.count += 1
                    cv2.imwrite(f"./runs/detect/predict/image{VideoCamera.count}.jpg", image) # 뒤에 image 넣을 것.
                if xbox >= 540 and flags == 1:
                    print('끝')
                    flags = 0
                
        ret, jpeg = cv2.imencode('.jpg', image)
        
        return jpeg.tobytes()