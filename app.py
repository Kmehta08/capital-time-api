from flask import Flask, request, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

# Secret token for auth
API_TOKEN = "supersecrettoken123"

# city-to-timezone mapping
city_timezones = {
    "Washington": "America/New_York",
    "London": "Europe/London",
    "Tokyo": "Asia/Tokyo",
    "Paris": "Europe/Paris",
    "Delhi": "Asia/Kolkata",
    "Canberra": "Australia/Sydney"
}

# Decorator for token check
def token_required(f):
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if auth_header and auth_header.startswith("Bearer "):
            token = auth_header.split(" ")[1]
            if token == API_TOKEN:
                return f(*args, **kwargs)
        return jsonify({"error": "Unauthorized"}), 401
    decorator.__name__ = f.__name__
    return decorator

@app.route('/api/time', methods=['GET'])
@token_required
def get_time():
    city = request.args.get("city")
    if city not in city_timezones:
        return jsonify({"error": f"City '{city}' not found in database"}), 404

    timezone = pytz.timezone(city_timezones[city])
    now = datetime.now(timezone)
    utc_offset = now.strftime('%z')
    utc_offset_formatted = f"UTC{utc_offset[:3]}:{utc_offset[3:]}"
    

    return jsonify({
        "city": city,
        "local_time": now.strftime('%Y-%m-%d %H:%M:%S'),
        "utc_offset": utc_offset_formatted
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
