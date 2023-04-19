# Using flask to make restapi in python
# import required libraries and functions to built restapi in python using flask
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

# on the terminal of typr to development mode: curl http://127.0.0.1:5000/
# returns hello world messege when we use GET.
# returns the data that we send when we use POST.
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":

        data = "hello world"
        return jsonify({"data_Start_after_post_use": data})


# A simple function  built to calculate the cube of a number
# the number to be cube is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 5
# this returns 125 (cube of 5)
@app.route("/home/<int:num>", methods=["GET"])
def disp(num):

    return jsonify({"data_Cuberoot": num**3})


# driver function
if __name__ == "__main__":

    app.run(debug=True)
