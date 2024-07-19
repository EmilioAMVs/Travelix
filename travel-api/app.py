from flask import Flask, request, jsonify
import os
import requests
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

def get_places(lat, lon, radius, keyword):
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'location': f'{lat},{lon}',
        'radius': radius,
        'type': keyword,
        'key': GOOGLE_API_KEY
    }
    response = requests.get(url, params=params)
    results = response.json()['results']
    places = []
    for place in results:
        place_details = {
            'place_id': place.get('place_id'),
            'name': place.get('name'),
            'description': place.get('vicinity'),
            'rating': place.get('rating'),
            'direction': '',  # You might need to make another API call to get directions
            'image': place.get('photos', [{}])[0].get('photo_reference', '')
        }
        places.append(place_details)
    return places

@app.route('/get_restaurants', methods=['GET'])
def get_restaurants():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    radius = request.args.get('radius')
    
    if not all([lat, lon, radius]):
        return jsonify({"error": "Missing required parameters"}), 400
    
    try:
        return jsonify(get_places(lat, lon, radius, 'restaurant'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_museums', methods=['GET'])
def get_museums():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    radius = request.args.get('radius')
    
    if not all([lat, lon, radius]):
        return jsonify({"error": "Missing required parameters"}), 400
    
    try:
        return jsonify(get_places(lat, lon, radius, 'museum'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get_parks', methods=['GET'])
def get_parks():
    lat = request.args.get('lat')
    lon = request.args.get('lon')
    radius = request.args.get('radius')
    
    if not all([lat, lon, radius]):
        return jsonify({"error": "Missing required parameters"}), 400
    
    try:
        return jsonify(get_places(lat, lon, radius, 'park'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)