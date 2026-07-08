from flask import Flask, render_template, request, abort
import requests

app = Flask(__name__)

API_URL = "https://flask-api-videogames.vercel.app/products"


def get_products():
    response = requests.get(API_URL, timeout=10)
    response.raise_for_status()
    return response.json()


@app.route("/")
def home():
    search = request.args.get("search", "").strip().lower()
    category = request.args.get("category", "").strip().lower()

    products = get_products()

    if search:
        products = [
            p for p in products
            if search in p.get("title", "").lower()
        ]

    if category and category != "todos":
        products = [
            p for p in products
            if category in p.get("title", "").lower()
        ]

    return render_template(
        "index.html",
        products=products,
        search=search,
        category=category
    )


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    products = get_products()

    product = next(
        (p for p in products if int(p.get("id", 0)) == product_id),
        None
    )

    if not product:
        abort(404)

    return render_template(
        "product.html",
        product=product
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template("index.html", products=[], search="", category=""), 404


if __name__ == "__main__":
    app.run(debug=True)