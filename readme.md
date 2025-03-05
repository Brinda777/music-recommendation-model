```md
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
```
│── .env                  # Environment variables (Spotify API credentials)
│── app.py                # Flask API for song recommendations
│── config.py             # Spotify API authentication setup
│── models.py             # KNN model training with song features
│── recommender.py        # Recommendation logic using KNN
│── accuracy.py           # Evaluation using Mean Average Precision (MAP)
│── spotify_helper.py     # Fetching song images from Spotify API
│── tracks.csv            # Dataset containing song features
│── README.md             # Project documentation
```

## 📌 Setup & Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/your-username/music-recommendation.git
cd music-recommendation
```

### 2️⃣ Create a Virtual Environment (Optional)  
```bash
python -m venv env
source env/bin/activate   # On macOS/Linux
env\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables  
Create a **.env** file in the project root and add your **Spotify API credentials**:  
```
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
```

### 5️⃣ Run the Flask API  
```bash
python app.py
```
The API will be accessible at:  
📍 **http://127.0.0.1:5000/recommend?song=YourSongName**  

## 🎯 API Usage  

### **Endpoint: Get Song Recommendations**  
#### Request:  
```http
GET /recommend?song={song_name}
```
#### Response Example:  
```json
{
  "recommended_songs": [
    {
      "song": "Song Title",
      "artist": "Artist Name",
      "image": "https://spotify-album-image-url.jpg"
    }
  ],
  "mean_average_precision": 0.85
}
```

## 🧪 Testing with Postman  
1. Open **Postman** and create a **GET request**.  
2. Enter the API endpoint:  
   ```
   http://127.0.0.1:5000/recommend?song=YourSongName
   ```
3. Click **Send** to receive recommendations.  

## 🔥 Evaluation Metric  
The system calculates **Mean Average Precision (MAP)** to measure the accuracy of recommendations. A **higher MAP score** means better recommendations.

## 📌 Future Improvements  
- Expand dataset with more song features.  
- Implement hybrid filtering (content + collaborative).  
- Deploy API on a cloud platform (e.g., AWS, Heroku).  

## 🤝 Contributing  
Feel free to **fork** this repository and contribute! If you find any issues, create a pull request or open an issue.  

## 📜 License  
This project is licensed under the **MIT License**.  
```






# Run command
- python app.py
