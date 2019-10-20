from aiohttp import web
import orjson
from models.resnet import load_model, score_model

model = load_model()

async def handle(request):
  try:
    txt = await request.text()
    json = orjson.loads(txt)
    result = score_model(model, json["data"])
    return web.json_response(result)
  except:
    print("ERROR")
    return web.json_response({ "error": True })

app = web.Application(client_max_size=100 * 1113559)
app.add_routes([web.post('/test', handle)])

if __name__ == '__main__':
    web.run_app(app)