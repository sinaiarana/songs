from flask import Flask, request, jsonify
import os
import json

app = Flask(__name__)
FILE_PATH = "songs.json"

# Initialize file if it doesn't exist
if not os.path.exists(FILE_PATH):
    with open(FILE_PATH, "w") as file:
        json.dump({}, file)

# Endpoint to update song data
@app.route("/update_song", methods=["POST"])
def update_song():
    data = request.json
    song_name = data.get("song", "").strip()
    if not song_name:
        return jsonify({"error": "No song provided"}), 400

    # Read existing data
    with open(FILE_PATH, "r") as file:
        songs = json.load(file)

    # Update song count
    if song_name in songs:
        songs[song_name] += 1
    else:
        songs[song_name] = 1

    # Save updated data
    with open(FILE_PATH, "w") as file:
        json.dump(songs, file)

    return jsonify({"message": "Song updated", "songs": songs})

# Endpoint to get song data
@app.route("/songs", methods=["GET"])
def get_songs():
    with open(FILE_PATH, "r") as file:
        songs = json.load(file)
    return jsonify(songs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
