from flask import Flask

application = Flask(__name__)


@application.route("/")
def index():
    myfile = open("index.html", mode='r')
    page   = myfile.read()
    myfile.close()
    return page