from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "https://flask-api-videogames.vercel.app/products"

@app.route("/")
def home():
    search = request.args.get("search", "").lower()

    response = requests.get(API_URL)
    products = response.json()

    if search:
        products = [
            p for p in products
            if search in p.get("title", "").lower()
        ]

    return render_template(
        "index.html",
        products=products,
        search=search
    )