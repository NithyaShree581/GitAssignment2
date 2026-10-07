from flask import Flask, request, jsonify
from asgiref.wsgi import WsgiToAsgi

app = Flask(__name__)

country_capitals = {
    "Delhi": "India",
    "Paris": "France",
    "London": "United Kingdom",
    "Tokyo": "Japan",
    "Berlin": "Germany"
}


@app.route("/country-capital", methods=["GET"])
def get_country():
    capital = request.args.get("capital")

    if not capital:
        return jsonify({"error": "Capital city is required"}), 400

    country = country_capitals.get(capital)

    if country:
        return jsonify({"country": country})

    return jsonify({"error": "Capital city not found"}), 404


asgi_app = WsgiToAsgi(app)