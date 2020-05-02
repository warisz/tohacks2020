from flask import render_template, Blueprint
from user.forms import UserForm

users = Blueprint('users', __name__)

@users.route("/", methods = ['GET', 'POST'])
def index():

    form = UserForm()

    if form.validate_on_submit():
        # TODO: Logic for the opencv stuff
        pass

    return render_template("test.html", form = form)