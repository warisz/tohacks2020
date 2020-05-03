from flask import render_template, Blueprint, Response
from user.forms import UserForm
from camera import VideoCamera
import time

users = Blueprint('users', __name__)

@users.route("/", methods = ['GET', 'POST'])
def index():

    form = UserForm()

    if form.validate_on_submit():
        # TODO: Logic for the opencv stuff
        pass

    return render_template("test.html", form = form)

def gen(camera):
    start = time.time()
    while True:
        delay = 3
        if (time.time() - start) >= delay:

            frame = camera.change_frame()
            yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
               

@users.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')