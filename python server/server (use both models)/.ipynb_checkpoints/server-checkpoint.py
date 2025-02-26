# server.py
from flask import Flask, request, jsonify, abort
import os
import tempfile
from songs.use_model import classify_song
from image.use_model import classify_emotions
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/classify_songs', methods=['POST'])
def upload_file():
    files = request.files.getlist('songs')
    results = []
    for file in files:
        with tempfile.NamedTemporaryFile(delete=False) as temp:
            file_path = temp.name
            file.save(file_path)
            emotion = classify_song(file_path)
            results.append(emotion)
        os.remove(file_path)

    return jsonify(results)


@app.route('/classify_images', methods=['POST'])
def classify_images():
    data = request.json
    try:
        emotion = classify_emotions(data['images'])
    except Exception:
        abort(404, description="No face detected")
    return {'emotion': emotion}


if __name__ == '__main__':
    app.run(debug=True)





