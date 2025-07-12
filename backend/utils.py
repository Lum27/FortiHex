from web3 import Web3

def verify_submission(challenge_id, submission):
    from challenges import challenges
    for challenge in challenges:
        if challenge["id"] == challenge_id:
            return challenge["solution"] == submission
    return False

def log_event(data):
    # Simulated logging (replace with smart contract interaction later)
    print(f"[SECURITY LOG] Challenge {data['challenge_id']} completed by {data.get('user_id', 'anonymous')}")
