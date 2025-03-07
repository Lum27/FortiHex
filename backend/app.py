from flask import Flask 
from flask_cors import CORS
import auth, challenges, leaderboard, logger, security, ai_anomaly, blockchain_logger, ipfs_storage, ipfs_retrieval, security_reports, threats_heatmap, alerts

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return {"message": "Welcome to FortiHex - Cybersecurity Training Platform"}

if __name__ == "__main__":
    app.run(debug=True)