from flask import Flask, render_template

# print(__name__)

app = Flask(__name__)

@app.route('/')
def index_page():
    return render_template(
        "index.html",
        the_title="My Site"
    )

@app.route('/product')
def product_page():
    return render_template(
        "product.html"
    )

@app.route('/contact')
def contact_page():
    return render_template(
        "contact.html"
    )

if __name__ == "__main__":
    app.run(debug=True)