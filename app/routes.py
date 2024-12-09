from flask import Blueprint, request, jsonify
from .services import login, fetch_profile, fetch_sport, fetch_match_odds

main_bp = Blueprint('main', __name__)

@main_bp.route('/api/login', methods=['POST'])
def login_user():
    data = request.json
    return login(data)

@main_bp.route('/api/profile', methods=['GET'])
def user_profile():
    cookies = request.headers.get('Cookie')
    return fetch_profile(cookies)

@main_bp.route('/api/sport', methods=['GET'])
def sports_data():
    user_id = request.args.get('userId')
    cookies = request.headers.get('Cookie')
    return fetch_sport(user_id, cookies)

@main_bp.route('/api/match-odds', methods=['GET'])
def match_odds():
    market_ids = request.args.get('marketId')
    cookies = request.headers.get('Cookie')
    return fetch_match_odds(market_ids, cookies)
