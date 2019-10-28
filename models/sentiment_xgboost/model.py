import joblib
import pandas as pd
from models.sentiment_xgboost.pipeline import TextSelector, NumberSelector, Tokenizer

def load_model():
    model = joblib.load('./assets/sentiment_xgboost/model.joblib.dat')
    return model

def score_model(model, inputs):
    X = pd.DataFrame()
    X['text'] = inputs
    X['len'] = [len(x.split()) for x in inputs]

    predictions = model.predict(X).reshape(-1)

    result = {
      "result": predictions.tolist()
    }

    return result