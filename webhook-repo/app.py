from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
from flask_cors import CORS
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
app = Flask(__name__)
CORS(app)

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]
collection = db[os.getenv("COLLECTION_NAME")]

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    event = request.headers.get("X-GitHub-Event")
    time = datetime.utcnow().strftime("%d %B %Y - %I:%M %p UTC")

    message = None

    if event == "push":
        author = data["pusher"]["name"]
        branch = data["ref"].split("/")[-1]
        message = f'{author} pushed to {branch} on {time}'

    elif event == "pull_request" and data["action"] == "opened":
        author = data["pull_request"]["user"]["login"]
        from_branch = data["pull_request"]["head"]["ref"]
        to_branch = data["pull_request"]["base"]["ref"]
        message = f'{author} submitted a pull request from {from_branch} to {to_branch} on {time}'

    elif event == "pull_request" and data["action"] == "closed" and data["pull_request"]["merged"]:
        author = data["pull_request"]["user"]["login"]
        from_branch = data["pull_request"]["head"]["ref"]
        to_branch = data["pull_request"]["base"]["ref"]
        message = f'{author} merged branch {from_branch} to {to_branch} on {time}'

    if message:
        collection.insert_one({"message": message})
        return jsonify({"msg": "Stored"}), 200

    return jsonify({"msg": "Ignored"}), 200

@app.route("/get-latest", methods=["GET"])
def get_latest():
    data = list(collection.find().sort("_id", -1).limit(10))
    return jsonify([d["message"] for d in data])

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(port=5000)
