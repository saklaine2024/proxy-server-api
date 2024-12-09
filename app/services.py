import requests
from flask import jsonify

# Define the base URL for your external site
BASE_URL = "https://vellke.com"

# Function to handle user login
def login(data):
    try:
        # POST request to login endpoint
        response = requests.post(f"{BASE_URL}/login", json=data, timeout=10)  # Added timeout of 10 seconds
        # Check if the response was successful
        if response.status_code == 200:
            return jsonify(response.json()), response.status_code
        else:
            return jsonify({"error": "Login failed", "details": response.json()}), response.status_code
    except requests.exceptions.RequestException as e:
        # Handle any exception that occurs during the request
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


# Function to fetch profile details for a logged-in user
def fetch_profile(cookies):
    headers = {"Cookie": cookies}
    try:
        # GET request to fetch profile data
        response = requests.get(f"{BASE_URL}/profile", headers=headers, timeout=10)  # Added timeout of 10 seconds
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
        # GET request to fetch sports data
        response = requests.get(f"{BASE_URL}/sport?userId={user_id}", headers=headers, timeout=10)  # Added timeout of 10 seconds
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
        # GET request to fetch match odds data
        response = requests.get(f"{BASE_URL}/match-odds?marketId={market_ids}&multi=true", headers=headers, timeout=10)  # Added timeout of 10 seconds
        if response.status_code == 200:
            return jsonify(response.json()), response.status_code
        else:
            return jsonify({"error": "Failed to fetch match odds", "details": response.json()}), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
