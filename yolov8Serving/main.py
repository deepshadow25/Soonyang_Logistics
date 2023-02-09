from flask import Flask, render_template, Response
from camera import VideoCamera
from ocr import OCRDetect
import os
import shutil

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

count = 0

def gen(camera):
    while True:
        if count % 3 == 0:
            frame = camera.get_frame()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpg\r\n\r\n' +frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    if os.path.exists("./runs/detect"):
            shutil.rmtree("./runs/detect")
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video_feed_2')
def ocr_feed():
    if os.path.exists("./runs/ocr_det"):
            shutil.rmtree("./runs/ocr_det")
    return Response(gen(OCRDetect()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)