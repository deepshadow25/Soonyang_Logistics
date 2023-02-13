import cv2
import torch
import numpy as np
from ultralytics import YOLO
from PIL import Image

model = YOLO("yolov8n.pt")
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
        #results = model(image)

        #print("result",type(image))
        #print("result",results)
        #a = np.squeeze(results.render())
        #count =0
        #count +=1
        #cv2.imwrite("frame%d.jpg" % count, image)
        #print("a",type(a))
        #print("a",a)

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
        # ret, jpeg = cv2.imencode('.jpg', image)
        
        
        model.predict(source=image, save=True) #욜로는 default로 /runs/detect/predict에 저장함
        
        #print(type(output))
        #print(output)
        #dst = cv2.imread( "./runs/detect/predict/image0.jpg")

        #pil_image=Image.fromarray(image)
        #image = np.array(image)
        #np_array.show()
        #print(type(dst))
        ret, jpeg = cv2.imencode('.jpg', image)
        
        return jpeg.tobytes()