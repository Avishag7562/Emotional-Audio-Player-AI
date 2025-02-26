from collections import Counter
import cv2
import numpy as np
import base64
import tensorflow as tf

# model = DeepFace.build_model("Emotion")

# Define emotion labels
emotion_labels = ['angry', 'happy', 'neutral', 'sad']

model = tf.keras.models.load_model(r"C:\Users\Avishag\OneDrive\final project\python server\server (use both models)\image\model.h5")

def image_preproccessing(image):
    '''get an image and return an image that prepared for the model'''
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    if len(faces)==0: raise Exception('No face have been detected')
    if len(faces)>1: raise Exception('Too many face have been detected')
    (x, y, w, h) = faces[0]
    face = gray_frame[y:y + h, x:x + w]
    resized_image = cv2.resize(face, (48, 48), interpolation=cv2.INTER_AREA)
    # cv2.imshow('Resized Image', resized_image)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    image = resized_image.reshape((1, 48, 48, 1))
    normalized_image = image / 255.0
    return normalized_image


def classify_emotion(image_b64):
    image_b64 = image_b64.split(",")[1]
    image_bytes = base64.b64decode(image_b64)
    nparr = np.frombuffer(image_bytes, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    print(image)
    preproccesed_image = image_preproccessing(image)
    prediction_idx = np.argmax(model.predict(preproccesed_image))
    prediction = emotion_labels[prediction_idx]
    return prediction


def most_frequent_element(arr):
    return Counter(arr).most_common(1)[0][0] if arr else None


def classify_emotions(images):
    emotions = []
    for image in images:
        emotion = classify_emotion(image['_imageAsDataUrl'])
        emotions.append(emotion)
    most_common_emotion = most_frequent_element(emotions)
    return most_common_emotion

