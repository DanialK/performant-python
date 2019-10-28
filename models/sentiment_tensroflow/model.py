import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import joblib
import json

def load_model():
    model = tf.keras.models.load_model("./assets/sentiment_tensorflow/model.h5")
    tokenizer = joblib.load('./assets/sentiment_tensorflow/tokenizer.pickle')
    with open('./assets/sentiment_tensorflow/configuration.json', 'r') as f:
        configuration = json.load(f)
    
    return model, tokenizer, configuration

def score_model(assets, x):
    model, tokenizer, configuration = assets
    MAX_SEQUENCE_LENGTH = configuration["MAX_SEQUENCE_LENGTH"]

    X_sample = tokenizer.texts_to_sequences(x)
    X_sample = pad_sequences(X_sample, maxlen=MAX_SEQUENCE_LENGTH)

    predictions = model.predict(X_sample).reshape(-1)

    result = {
      "result": predictions.tolist()
    }

    return result