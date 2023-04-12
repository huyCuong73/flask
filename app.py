from flask import Flask
from route import route

app = Flask(__name__)
app.config['DEBUG'] = True

route(app)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World1asdsa</p>"

    

