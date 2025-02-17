# **🎵 Music Recommendation Model**  

This repository contains the core machine learning model for the **Madhur Music Recommendation System**, which provides personalized song recommendations using **content-based filtering and item-based collaborative filtering**. The model processes song attributes and user interactions to generate relevant music suggestions.  


## **📌 Features**  
- **Hybrid Recommendation System**: Uses **content-based filtering** (analyzing song features like danceability, energy, and tempo) and **collaborative filtering** (learning from similar users).  
- **Optimized Data Processing**: Reduces memory usage and speeds up calculations.  
- **Scalable Similarity Calculation**: Uses **cosine similarity** on a large dataset to find the most relevant songs.  
- **Integration with FastAPI**: Can be connected to an API for real-time recommendations.  

## **📂 Project Structure**  
- **`app.py`** → Loads and processes the dataset, reducing memory usage.  
- **`similarity.py`** → Computes the **cosine similarity** between songs using audio features.  
- **`similarity-npz.py`** → Converts and stores similarity data efficiently in a **compressed sparse matrix** format.  
- **`recommendation.py`** → FastAPI backend that handles requests and returns music recommendations.  
- **`dataset.csv`** → The dataset containing song features and metadata (not included in the repo).
  
## **⚙️ Setup & Installation**  
### **🔹 Prerequisites**  
Ensure you have **Python 3.8+** installed, along with the required dependencies:  
```bash
pip install -r requirements.txt
```

### **🔹 Running the Model**  
1. **Clone the repository**  
   ```bash
   git clone https://github.com/Brinda777/music-recommendation-model.git  
   cd music-recommendation-model  
   ```

2. **Prepare the dataset**  
   - Place your dataset as `dataset.csv` in the project directory.  

3. **Preprocess the data**  
   ```bash
   python app.py
   ```
   This will clean the dataset and save it as `df.pkl`.  

4. **Compute similarity matrix**  
   ```bash
   python similarity.py
   ```
   This generates the similarity matrix and stores it in a compressed format.  

5. **Convert similarity matrix to `.npz` format**  
   ```bash
   python similarity-npz.py
   ```
   
6. **Run the recommendation API**  
   ```bash
   uvicorn recommendation:app --host 0.0.0.0 --port 8000 --reload
   ```
   The API will be available at `http://localhost:8000/`.  

## **🚀 API Endpoints**  
| Method | Endpoint | Description |  
|--------|---------|-------------|  
| `POST` | `/get_options` | Returns a list of matching songs based on a search query. |  
| `POST` | `/get_recommendations` | Provides top **10** recommended songs for a selected track. |  

## **🛠 Future Enhancements**  
- Improve recommendation accuracy with **deep learning** models.  
- Introduce **real-time user feedback** to refine recommendations.  
- Implement **user-based preference tracking** to adapt to listening habits.  

🎵 **Enjoy smart and personalized music recommendations!** 🎵  

