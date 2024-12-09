from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Define the base URL for your external site
BASE_URL = "https://vellke.com"

@app.route('/')
def home():
    return "Welcome to the Proxy Server!"

# Route for user login
@app.route('/login', methods=['POST'])
def login_route():
    data = request.get_json()  # Get data sent in the POST request
    return login(data)  # Call the login function

# Route to fetch profile details
@app.route('/profile', methods=['GET'])
def profile_route():
    cookies = request.args.get('cookies')  # Get cookies from query parameters
    if not cookies:
        return jsonify({"error": "Cookies parameter is required"}), 400
    return fetch_profile(cookies)

# Route to fetch sports data
@app.route('/sport', methods=['GET'])
def sport_route():
    user_id = request.args.get('userId')  # Get userId from query parameters
    cookies = request.args.get('cookies')  # Get cookies from query parameters
    if not user_id or not cookies:
        return jsonify({"error": "userId and cookies are required"}), 400
    return fetch_sport(user_id, cookies)

# Route to fetch match odds
@app.route('/match-odds', methods=['GET'])
def match_odds_route():
    market_ids = request.args.get('marketIds')  # Get marketIds from query parameters
    cookies = request.args.get('cookies')  # Get cookies from query parameters
    if not market_ids or not cookies:
        return jsonify({"error": "marketIds and cookies are required"}), 400
    return fetch_match_odds(market_ids, cookies)

# Function to handle user login
def login(data):
    try:
        response = requests.post(f"{BASE_URL}/login", json=data, timeout=10)
        if response.status_code == 200:
            return jsonify(response.json()), response.status_code
        else:
            return jsonify({"error": "Login failed", "details": response.json()}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Function to fetch profile details for a logged-in user
def fetch_profile(cookies):
    headers = {"Cookie": cookies}
    try:
        response = requests.get(f"{BASE_URL}/profile", headers=headers, timeout=10)
        if response.status_code == 200:
            return jsonify(response.json()), response.status_code
        else:
            return jsonify({"error": "Failed to fetch profile", "details": response.json()}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Function to fetch sports data for a specific user
def fetch_sport(user_id, cookies):
    headers = {"Cookie": cookies}
    try:
        response = requests.get(f"{BASE_URL}/sport?userId={user_id}", headers=headers, timeout=10)
        if response.status_code == 200:
            return jsonify(response.json()), response.status_code
        else:
            return jsonify({"error": "Failed to fetch sports data", "details": response.json()}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

# Function to fetch match odds based on market IDs
def fetch_match_odds(market_ids, cookies):
    headers = {"Cookie": cookies}
    try:
        response = requests.get(f"{BASE_URL}/match-odds?marketId={market_ids}&multi=true", headers=headers, timeout=10)
        if response.status_code == 200:
            return jsonify(response.json()), response.status_code
        else:
            return jsonify({"error": "Failed to fetch match odds", "details": response.json()}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)
