import os

import requests
from flask import Flask, abort, render_template, request

app = Flask(__name__)

API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "https://flask-api-videogames.vercel.app"
)


@app.route("/")
def home():
    search = request.args.get("q", "").strip()
    category = request.args.get("category", "").strip().lower()

    query = search or category

    try:
        if query:
            response = requests.get(
                f"{API_BASE_URL}/search",
                params={"q": query},
                timeout=15
            )
        else:
            response = requests.get(
                f"{API_BASE_URL}/products",
                timeout=15
            )

        response.raise_for_status()
        products = response.json()

        if not isinstance(products, list):
            products = []

    except requests.RequestException as error:
        app.logger.exception("API request failed: %s", error)

        return render_template(
            "index.html",
            products=[],
            search=search,
            category=category,
            api_error="No fue posible cargar los productos."
        ), 502

    return render_template(
        "index.html",
        products=products,
        search=search,
        category=category,
        api_error=None
    )


@app.route("/product/<int:product_id>")
def product_detail(product_id):
    try:
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

        history = history_response.json() if history_response.ok else []

    except requests.RequestException:
        abort(502)

    return render_template(
        "product.html",
        product_data=product_data,
        history=history
    )


if __name__ == "__main__":
    app.run(debug=True)