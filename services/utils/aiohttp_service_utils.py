from aiohttp import web
import orjson

def create_aiohttp_service(load_model, score_model):
    async def handle(request):
        txt = await request.text()
        json = orjson.loads(txt)
        result = score_model(model, json["data"])
        return web.json_response(result)

    model = load_model()
    app = web.Application(client_max_size=100 * 1113559)
    app.add_routes([web.post('/score', handle)])

    return app
    