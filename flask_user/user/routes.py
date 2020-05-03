from flask import render_template, Blueprint, Response, redirect, url_for
from user.forms import UserForm
from camera import VideoCamera
import time
import matplotlib
import matplotlib.pyplot as mpl
import numpy as np

users = Blueprint('users', __name__)
emotionDict = {"joy": 0, "surprise": 0, "sorrow": 0, "anger": 0}
allEmotionDicts = {}

@users.route("/", methods = ['GET', 'POST'])
def index():

    form = UserForm()

    if form.validate_on_submit():
        allEmotionDicts[str(UserForm.url)] = emotionDict
        graphing()
        reset()
        pass
        
    
    return render_template("test.html", form = form)

def graphing():

    counter = 0
    for key, value in allEmotionDicts.items():
        #creates a new figure
        figure = mpl.figure()
        figure.suptitle("Emotions for " + str(key))

        figure, axes = mpl.subplots(1,1) #makes a 1x1 figure

        #setting axis labels
        axes.set_xlabel('Emotions')
        axes.set_ylabel('Seconds')
        axes.set_ylim(0,100)

        #plotting a point - 'bo' means blue plot
        for key2, value2 in value.items():
            axes.plot(key2, value2, 'bo')


        #CREATES FILE ---> CHECK gradesGraph.png
        figure.savefig("graph" + str(counter) + ".png")
        counter+=1

def reset():
    emotionDict = {"joy": 0, "surprise": 0, "sorrow": 0, "anger": 0}

def gen(camera):
    start = time.time()
    while True:
        delay = 3
        if (time.time() - start) >= delay:

            frame = (camera.change_frame())[0]
            emotion = (camera.change_frame())[1]

            if emotion != "":
                emotionDict[emotion] += 1

            print(emotionDict)
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
               

@users.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

