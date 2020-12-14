from flask import Flask, render_template

# print(__name__)

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template(
        "index.html",
        the_title="My Site"
    )

if __name__ == "__main__":
    app.run(debug=True)