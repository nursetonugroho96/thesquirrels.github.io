from flask import Flask, render_template
import json
import urllib.request as request
import os
import ssl

app = Flask(__name__)

api_key = "bba89bfe21b4ecd6fb95bbe12caf06a0"
base_url = "https://api.themoviedb.org/3/discover/movie?api_key=" + api_key

@app.route("/")
def home():
    ssl._create_default_https_context = ssl._create_unverified_context
    response = request.urlopen(base_url, context=ssl._create_unverified_context())
    json_data = json.loads(response.read())
    return render_template("index.html", data=json_data["results"])

if __name__ == "__main__":
    app.run(debug=True)
