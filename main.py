from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    data = [] #'100', '200', '300', '400']
    return render_template(
        "index.html", 
        name=request.args["name"], 
        lastname=request.args["lastname"],
        data=data)

if __name__ == "__main__":
    app.run(debug=True)