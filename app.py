import os
import requests
from flask import Flask, render_template, request, abort

app = Flask(__name__)

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://flask-api-videogames.vercel.app"
)


@app.route("/")
def home():
    search = request.args.get("q", "").strip()

    if search:
        url = f"{API_BASE_URL}/search"
        response = requests.get(url, params={"q": search}, timeout=15)
    else:
        url = f"{API_BASE_URL}/products"
        response = requests.get(url, timeout=15)

    response.raise_for_status()
    products = response.json()

    return render_template(
        "index.html",
        products=products,
        search=search
    )


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    response = requests.get(
        f"{API_BASE_URL}/products/{product_id}",
        timeout=15
    )

    if response.status_code == 404:
        abort(404)

    response.raise_for_status()
    product_data = response.json()

    history_response = requests.get(
        f"{API_BASE_URL}/products/{product_id}/history",
        timeout=15
    )

    history = []

    if history_response.ok:
        history = history_response.json()

    return render_template(
        "product.html",
        product_data=product_data,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)