from flask import Flask, jsonify
import requests

app = Flask(__name)

@app.route('/top-songs', methods=['GET'])
def get_top_songs():
    deezer_api_key = 'YOUR_DEEZER_API_KEY'
    headers = {
        'X-RapidAPI-Key': deezer_api_key
    }

    response = requests.get('https://api.deezer.com/chart/0/tracks', headers=headers)

    if response.status_code == 200:
        top_10_songs = response.json()
        return jsonify(top_10_songs)
    else:
        return "Error: Unable to retrieve data."

if __name__ == '__main__':
    app.run()


