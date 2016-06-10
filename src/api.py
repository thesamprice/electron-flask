from flask import Flask,render_template
from flask_restful import Resource, Api
from flask_cors import CORS, cross_origin
from flask.ext.bower import Bower
from flask.ext import assets
import os

app = Flask(__name__)
env = assets.Environment(app)
#env = app
# Tell flask-assets where to look for our coffeescript and sass files.
env.load_path = [
    os.path.join(os.path.dirname(__file__), 'static/bower_components'),
    os.path.join(os.path.dirname(__file__), 'static'),
]
env.register(
    'js_all',
    assets.Bundle(
        'jquery/dist/jquery.min.js',
        output='built/js_all.js'
    )
)
env.register(
    'css_all',
    assets.Bundle(
        'css/main.css',
        output='built/css_all.css'
    )
)

Bower(app)
CORS(app)
api = Api(app)

@app.route("/")
def index():
    txt = render_template('index.html')
    return txt

@api.resource('/HelloWorld')
class HelloWorld(Resource):
    def get(self):
        print "HELLOWORLD "
        return {'hello': 'world'}



if __name__ == "__main__":
    app.run(debug=True)
