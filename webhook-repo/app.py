from flask import Flask, request, jsonify, render_template
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient(os.getenv("MONGO_URI"))
db = client["webhookDB"]
collection = db["events"]

# Route to serve the frontend HTML
@app.route('/')
def index():
    return render_template('index.html')  # Make sure you have index.html in /templates

# Webhook endpoint from GitHub
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        return "Webhook endpoint - POST your events here.", 200

    # Your existing POST handling code below
    data = request.json

    if 'commits' in data:  # PUSH event
        for commit in data['commits']:
            doc = {
                "type": "push",
                "author": commit['author']['name'],
                "to_branch": data['ref'].split('/')[-1],
                "timestamp": commit['timestamp']
            }
            collection.insert_one(doc)

    elif 'pull_request' in data:  # PULL REQUEST or MERGE event
        action_type = "merge" if data['action'] == "closed" and data['pull_request']['merged'] else "pull_request"
        doc = {
            "type": action_type,
            "author": data['pull_request']['user']['login'],
            "from_branch": data['pull_request']['head']['ref'],
            "to_branch": data['pull_request']['base']['ref'],
            "timestamp": data['pull_request']['updated_at']
        }
        collection.insert_one(doc)

    return jsonify({"status": "success"}), 200

# Endpoint to get raw events JSON
@app.route('/events', methods=['GET'])
def get_events():
    events = list(collection.find({}, {'_id': 0}))
    return jsonify(events)

# New route to display events nicely in a webpage
@app.route('/view-events')
def view_events():
    return render_template('events.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
