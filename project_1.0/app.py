from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def first():
    return render_template(
        "index.html",
        the_title="My Site"
    )

app.run(debug=True)