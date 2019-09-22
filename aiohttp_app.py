from aiohttp import web
import orjson

async def handle(request):
  json = orjson.loads(await request.text())
  return web.Response(text=json["name"])

app = web.Application()
app.add_routes([web.post('/test', handle)])

if __name__ == '__main__':
    web.run_app(app)