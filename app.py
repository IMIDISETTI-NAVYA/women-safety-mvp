from flask import Flask, render_template
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Firebase Init
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

@app.route("/")
def home():
    return "Women Safety App is Running"

@app.route("/driver/<driver_id>")
def driver_page(driver_id):

    # 🔥 IMPORTANT FIX
    driver_id = driver_id.upper()

    doc = db.collection("drivers").document(driver_id).get()

    if not doc.exists:
        return "Driver Not Found"

    data = doc.to_dict()

    return render_template(
        "driver.html",
        name=data.get("name", "Unknown"),
        auto=data.get("auto", "Unknown"),
        phone=data.get("phone", "Not Available"),
        verified=data.get("verified", False)
    )

if __name__ == "__main__":
    app.run(debug=True)
