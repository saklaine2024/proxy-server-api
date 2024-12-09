from flask import Flask, jsonify, request
from services import login, fetch_profile, fetch_sport, fetch_match_odds

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Proxy Server!"

# Route for user login
@app.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()
    return login(data)

# Route to fetch profile details
@app.route('/profile', methods=['GET'])
def profile_route():
    cookies = request.args.get('cookies')
    if not cookies:
        return jsonify({"error": "Cookies parameter is required"}), 400
    return fetch_profile(cookies)

# Route to fetch sports data
@app.route('/sport', methods=['GET'])
def sport_route():
    user_id = request.args.get('userId')
    cookies = request.args.get('cookies')
    if not user_id or not cookies:
        return jsonify({"error": "userId and cookies are required"}), 400
    return fetch_sport(user_id, cookies)

# Route to fetch match odds
@app.route('/match-odds', methods=['GET'])
def match_odds_route():
    market_ids = request.args.get('marketIds')
    cookies = request.args.get('cookies')
    if not market_ids or not cookies:
        return jsonify({"error": "marketIds and cookies are required"}), 400
    return fetch_match_odds(market_ids, cookies)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
