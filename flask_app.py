from flask import Flask
from flask import request
import orjson

app = Flask(__name__)

@app.route('/test', methods = ['POST'])
def test():
  val = request.get_json()
  return val


if __name__ == '__main__':
  app.run(host='0.0.0.0', port= 8080)