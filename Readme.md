# 🔔 GitHub Webhook Listener – Flask + MongoDB 

A lightweight, real-time GitHub webhook listener built with **Flask**, which captures events like **push**, **pull request**, and **merge** from a GitHub repository and displays the latest activity in a minimal web UI. Events are stored in **MongoDB** and fetched by the UI every 15 seconds.

---

## 📌 Features

- 🔁 Receives GitHub webhooks for `push`, `pull_request`, and `merge`
- 📥 Stores messages in MongoDB
- 💻 Minimal frontend UI to view activity logs
- 🔄 Frontend updates every 15 seconds using polling
- 🌐 Uses **ngrok** for exposing local Flask server to GitHub
- ✅ Clean, professional codebase with `.env` support

---

## 🏗️ Project Structure

webhook-repo/
├── app.py # Flask app and routes
├── .env # MongoDB credentials
├── requirements.txt # Python dependencies
├── templates/
│ └── index.html # Frontend UI


2️⃣ Create Virtual Environment & Install Dependencies
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate       # On Windows
pip install -r requirements.txt


3️⃣ Setup MongoDB & .env File
Make sure MongoDB is running locally or use MongoDB Atlas.

Create a .env file:

env
Copy
Edit
MONGO_URI=mongodb://localhost:27017
DB_NAME=webhook_db
COLLECTION_NAME=events


4️⃣ Run the Flask App
bash
Copy
Edit
python app.py


5️⃣ Start ngrok Tunnel (for GitHub Webhook)
In a new terminal:

bash
Copy
Edit
ngrok http 5000
🔗 Copy the HTTPS URL (e.g., https://abcd1234.ngrok-free.app)




6️⃣ Add Webhook to Your GitHub Repository (action-repo)
Go to GitHub action-repo → Settings → Webhooks → Add webhook

Use this:

Field	Value
Payload URL	https://abcd1234.ngrok-free.app/webhook
Content type	application/json
Secret	(leave blank)
Events	Push, Pull , Merge Request



💻 Frontend Preview
Visit http://localhost:5000
The page will auto-refresh every 15 seconds and show new webhook messages.



