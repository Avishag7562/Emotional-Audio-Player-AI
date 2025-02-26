import  joblib
import pandas as pd
model = joblib.load('./rmodel.joblib')
scaler = joblib.load('./fitted_scaler.save')

df = pd.read_csv(r"C:\Users\Avishag\OneDrive\songs_data.csv")

x = df.drop(['Unnamed: 0', 'id', 'class', 'label', 'song_name'], axis=1)
y = df['class']

x = pd.DataFrame(scaler.transform(x))


num_song = x.iloc[1, :]
lable_song = y[1]
pred_val = model.predict(num_song.values.reshape(1, -1))[0]

print(' Random Forest Classifier\n')
print("Emotion of song is:" ,pred_val, ",True Emotion is:", lable_song )

