from flask import Flask, render_template, request

import json

from bokeh.embed import json_item
from bokeh.plotting import figure
from bokeh.sampledata.iris import flowers

app = Flask(__name__)

colormap = {'setosa': 'red', 'versicolor': 'green', 'virginica': 'blue'}
colors = [colormap[x] for x in flowers['species']]

def make_plot(x, y):
    p = figure(
        title="Iris Morphology",
        sizing_mode="fixed",
        plot_width=400,
        plot_height=400
    )
    p.xaxis.axis_label = x
    p.yaxis.axis_label = y
    p.circle(flowers[x], flowers[y], color=colors, fill_alpha=0.2, size=10)
    return p

@app.route("/")
def root():
    return render_template(
        "page_1.html"
    )

@app.route("/plot")
def plot():
    p = make_plot("petal_width", "petal_length")
    return json.dumps(json_item(p, "myplot"))

@app.route("/plot2")
def plot2():
    p = make_plot("sepal_width", "sepal_length")
    return json.dumps(json_item(p))

@app.route("/test")
def test():
    data = ['100', '200', '300', '400']
    return render_template(
        "test.html", 
        name=request.args["name"], 
        lastname=request.args["lastname"],
        data=data
    )

if __name__ == "__main__":
    app.run()