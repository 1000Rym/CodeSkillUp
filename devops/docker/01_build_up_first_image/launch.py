from distutils.log import debug
from flask import Flask
hello_world = Flask(__name__)

@hello_world.route("/")
def run():
    return "Hello World, I am Benedict!"


if __name__ == '__main__':
    hello_world.run(host="0.0.0.0", port=3000, debug=True)