import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors

## KNN MODEL

# Load the dataset
df = pd.read_csv("tracks.csv")

# Feature selection and handle missing values
features = ['danceability', 'energy', 'tempo']
df[features] = df[features].fillna(df[features].mean())

# Normalize features
scaler = StandardScaler()
df[features] = scaler.fit_transform(df[features])

# Train KNN Model
knn = NearestNeighbors(n_neighbors=6, metric='cosine', algorithm='brute')
knn.fit(df[features])
