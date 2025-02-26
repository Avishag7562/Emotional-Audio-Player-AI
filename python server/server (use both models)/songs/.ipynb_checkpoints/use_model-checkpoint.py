import  joblib
import pandas as pd
from songs.featureExtractionSong import extract_feature_song

model = joblib.load(r'./songs/rmodel.joblib')
scaler = joblib.load('./songs/fitted_scaler.save')

def classify_song(song_path):
    file = pd.DataFrame(extract_feature_song(song_path))
    file = pd.DataFrame(scaler.transform(file)) #scale
    song = file.iloc[0, :]

    pred_val = model.predict(song.values.reshape(1, -1))[0]
    return pred_val



