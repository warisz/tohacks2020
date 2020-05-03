import cv2
faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

class VideoCamera(object):
    def __init__(self):
       self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()

    def change_frame(self):
        ret, frame = self.video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        face = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(35, 35))

        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (w+x, h+y), (200, 50, 30), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        return jpeg.tobytes()




