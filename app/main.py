from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Flask Backend, Hi from rsingh95!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)