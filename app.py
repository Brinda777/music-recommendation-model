from flask import Flask, request, jsonify
from recommender import recommend_songs

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    song_name = request.args.get('song')
    if not song_name:
        return jsonify({"error": "Please provide a song name."}), 400

    recommendations = recommend_songs(song_name)
    if not recommendations:
        return jsonify({"error": "Song not found in the dataset."}), 404

    return jsonify({"recommended_songs": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
