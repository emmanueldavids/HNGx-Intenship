# app/routes.py
from flask import render_template, request, jsonify
import datetime
import pytz

from app import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Validate inputs
    if not slack_name or not track:
        return jsonify({"error": "slack_name and track query parameters are required."}), 400

    # Get current day of the week
    current_day = datetime.datetime.now(pytz.utc).strftime("%A")

    # Get current UTC time with validation of +/-2 minutes
    current_time = datetime.datetime.now(pytz.utc)
    valid_time = current_time - datetime.timedelta(minutes=2)
    valid_time = valid_time.replace(microsecond=0)
    current_time_str = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")

    # GitHub URLs
    github_repo_url = "https://github.com/emmanueldavids/HNGx-Intenship"
    github_file_url = f"{github_repo_url}/app/routes.py"

    # Response JSON
    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": current_time_str,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)
