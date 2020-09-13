import json

from flask import Flask, render_template, request


app = Flask(__name__)


# @app.route("/")
# def hello():
#     return "Hello, Flask!"


@app.route("/")
def home():
    return render_template(
        "index.html"
    )


@app.route("/test")
def test():
    # for example: http://localhost:5000/test?name=Ivan&lastname=Ivanov
    data = [] #'100', '200', '300', '400']
    return render_template(
        "test.html", 
        name=request.args["name"], 
        lastname=request.args["lastname"],
        data=data
    )


if __name__ == "__main__":
    app.run(debug=True)