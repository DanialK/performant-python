from flask import Flask, jsonify, request
from models.resnet import load_model, score_model

model = load_model()

app = Flask(__name__)

@app.route('/score', methods = ['POST'])
def test():
  try:
    json = request.get_json(force=True)
    x = json["data"]
    result = score_model(model, x)
    resp = jsonify(result)
    return resp
  except:
    print("ERROR")
    return { "error": True }


if __name__ == '__main__':
  app.run(host='0.0.0.0', port= 8080)