from flask import Flask, request, jsonify
from challenges import challenges
from utils import verify_submission, log_event

app = Flask(__name__)

@app.route('/challenges', methods=['GET'])
def get_challenges():
    return jsonify(challenges)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    challenge_id = data.get('challenge_id')
    submission = data.get('submission')

    if verify_submission(challenge_id, submission):
        log_event(data)
        return jsonify({"result": "Success", "message": "Challenge completed!"})
    else:
        return jsonify({"result": "Failure", "message": "Try again!"}), 400

if __name__ == '__main__':
    app.run(debug=True)
