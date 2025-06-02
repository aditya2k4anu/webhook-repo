# Webhook Repo

This repository contains the webhook endpoint server to capture GitHub repository events (Push, Pull Request, Merge) via GitHub Webhooks. The events are stored in a MongoDB database and can be viewed via a simple frontend dashboard.

---

## Features

- Receives GitHub webhook events for Push and Pull Requests.
- Stores event data in MongoDB.
- Provides a frontend dashboard to view recent events.
- Uses Flask as backend server.

---

## Setup Instructions

1. **Clone this repository:**

```bash
git clone https://github.com/your-username/webhook-repo.git
cd webhook-repo
Create a virtual environment and install dependencies:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate
pip install -r requirements.txt
Create a .env file in the root directory with MongoDB URI:

ini
Copy
Edit
MONGO_URI=your_mongodb_connection_string
Run the Flask server:

bash
Copy
Edit
python app.py
Expose your local server to the internet using ngrok (or similar tool):

bash
Copy
Edit
ngrok http 5000
Set the ngrok forwarding URL as the webhook URL in your GitHub repository settings:

arduino
Copy
Edit
https://your-ngrok-url.ngrok-free.app/webhook
Usage
The server listens for GitHub webhook POST requests on /webhook.

Event data is stored in MongoDB collection events.

Access the dashboard at http://localhost:5000/ to see the stored events.

Notes
Make sure your GitHub webhook is configured to send Push and Pull Request events.

Secure your MongoDB URI and do not expose sensitive credentials in public repos.

This project is for educational/demo purposes.

Contact
For any questions or issues, please contact Your Name.

go
Copy
Edit

Just replace `your-username`, `your_mongodb_connection_string`, `your-ngrok-url`, and your contact info before committing!









Tools


