from flask import Flask, request, jsonify
from recommender import recommend_songs
from accuracy import mean_average_precision


app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    song_name = request.args.get('song')
    if not song_name:
        return jsonify({"error": "Please provide a song name."}), 400

    recommendations, relevant_songs = recommend_songs(song_name)
    if not recommendations:
        return jsonify({"error": "Song not found in the dataset."}), 404

    # Compute MAP Score
    recommended_names = [rec["song"] for rec in recommendations]
    map_score = mean_average_precision([recommended_names], [relevant_songs])

    return jsonify({
        "recommended_songs": recommendations,
        "mean_average_precision": round(map_score, 4)  # Round for readability
    })

if __name__ == "__main__":
    app.run(debug=True)
