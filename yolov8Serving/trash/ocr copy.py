import cv2
import torch
import numpy as np
from ultralytics import YOLO
from PIL import Image

model = YOLO("result/tracking_num.pt")
#model = torch.load('../result/yolov5s.pt')
#model.eval()
#model = torch.hub.load('./yolov5', 'custom','./result/yolov5l_best.pt', source='local')

class OCRDetect(object):
    
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
        success, frame = self.video.read()
        #image=cv2.flip(image, -1)
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
        
        result = model.predict(source=frame, save=True) #욜로는 default로 /runs/detect/predict에 저장함

        boxes = result[0].boxes
        
        #shape확인 tensor([[1351.50000,  123.50000,  245.00000,   33.00000]])
        
        if len(boxes) > 0 :
            flags = 0
            count = 0
            for i in range(len(boxes)):
                print(i+1,"번째 박스")
                box = boxes[i]
                x1 = box.xyxy[0][0] # xmin값
                y1 = box.xyxy[0][1]
                x2 = box.xyxy[0][2]
                y2 = box.xyxy[0][3]
                #IndexError: invalid index of a 0-dim tensor. Use `tensor.item()` in Python or `tensor.item<T>()` in C++ to convert a 0-dim tensor to a number
                #텐서화
                x1 = x1.item()
                y1 = y1.item()
                x2 = x2.item()
                y2 = y2.item()
                #print('shape확인@@@@@@@@',x1, y1, x2, y2) , 결과 shape확인@@@@@@@@ 801.0 241.0 1113.0 279.0 float 형
                x1 = int(x1)
                y1 = int(y1)
                x2 = int(x2)
                y2 = int(y2)
                print(x1,y1,x2,y2,type(x1))
                
                xbox = (x1+x2)/2   # x 중심좌표
                #img.shape  (세로:1080, 가로:1920, 3)
                if xbox>= 480 or xbox <=1440 and flags == 0:
                    print('중간')
                    flags = 1
                    count += 1
                    img = cv2.imread("/Users/kdb/projectserving/runs/detect/predict/image0.jpg")
                    #바운딩 
                    
                    path = "/Users/kdb/projectserving/ocr/cropimage.jpg"
                    img = img[y1:y2,x1:x2]
                    cv2.imwrite(path,img)

                if xbox >= 1440 and flags == 1:
                    print('끝')
                    flags = 0

                    
                        
                        
                   
                    
        dst = cv2.imread( "./runs/detect/predict2/image0.jpg")
        ret, jpeg = cv2.imencode('.jpg', frame)
        
        return jpeg.tobytes()