from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np

def load_model():
    model = ResNet50(weights='imagenet')
    return model

def score_model(model, x):
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    predictions = model.predict(x)
    result = {
      "result": [ [x[1], round(x[2] * 100, 2)] for x in decode_predictions(predictions, top=3)[0]]
    }
    return result