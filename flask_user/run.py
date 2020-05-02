from flask import Flask

app = Flask(__name__, template_folder='templates')

from user.routes import users

app.register_blueprint(users)

app.config['SECRET_KEY'] = "fdsfdsakgklgw"

if __name__ == '__main__':
    app.run(debug=True)