
from flask import Flask, jsonify, request
from models.resnet import load_model, score_model

def flask_service_creator(load_model, score_model):
    model = load_model()
    app = Flask(__name__)

    @app.route('/score', methods = ['POST'])
    def handle():
        json = request.get_json(force=True)
        x = json["data"]
        result = score_model(model, x)
        resp = jsonify(result)
        return resp

    return app
