# utils.py

def login(data):
    # Add your login logic here
    return jsonify({"message": "Logged in successfully!"})

def fetch_profile(cookies):
    # Add your profile fetching logic here
    return jsonify({"profile": "User Profile Data"})

def fetch_sport(user_id, cookies):
    # Add your sport fetching logic here
    return jsonify({"sport": "Sports Data"})

def fetch_match_odds(market_ids, cookies):
    # Add your match odds fetching logic here
    return jsonify({"match_odds": "Match Odds Data"})
