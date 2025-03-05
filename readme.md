# 🎵 Music Recommendation System  

This project is a **content-based music recommendation system** that suggests similar songs based on audio features like **danceability, energy, and tempo**. It uses **K-Nearest Neighbors (KNN)** for recommendations and integrates with the **Spotify API** to fetch album cover images. The system is served through a **Flask API** and evaluated using **Mean Average Precision (MAP)**.

## 🚀 Features  
- **Song Recommendations**: Suggests similar tracks based on audio features.  
- **Spotify API Integration**: Fetches album cover images for recommended songs.  
- **KNN Model**: Uses Euclidean distance to find similar songs.  
- **Flask API**: Provides recommendations via a RESTful API.  
- **Evaluation Metrics**: Computes **Mean Average Precision (MAP)** for accuracy.  
- **Postman Testing**: API endpoints can be tested in **Postman**.  

## 🛠️ Tech Stack  
- **Python** (Pandas, NumPy, Scikit-learn)  
- **Flask** (for the API)  
- **Spotipy** (Spotify API integration)  
- **Postman** (for testing)  
 
## 📂 Project Structure  
```plaintext
│── .env                  # Environment variables (Spotify API credentials)
│── app.py                # Flask API for song recommendations
│── config.py             # Spotify API authentication setup
│── models.py             # KNN model training with song features
│── recommender.py        # Recommendation logic using KNN
│── accuracy.py           # Evaluation using Mean Average Precision (MAP)
│── spotify_helper.py     # Fetching song images from Spotify API
│── tracks.csv            # Dataset containing song features
│── README.md             # Project documentation

## 📌 Setup & Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/music-recommendation.git
cd music-recommendation






