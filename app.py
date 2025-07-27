import requests
from flask import Flask,jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Fun & Advice Page"

@app.route("/joke")
def joke():
    joke_url = "https://official-joke-api.appspot.com/random_joke"
    res = requests.get(joke_url)
    data = res.json()
    return jsonify({
        "setup":data["setup"],
        "punchline":data["punchline"]
    })

@app.route("/advice")
def advice():
    advice_url = "https://api.adviceslip.com/advice"
    res = requests.get(advice_url)
    data = res.json()

    return jsonify({
        "advice":data["slip"]["advice"]
    })

if __name__=="__main__":
    app.run(port=5000,debug=True)