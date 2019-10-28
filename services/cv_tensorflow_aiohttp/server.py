from aiohttp import web

from services.utils.aiohttp_service_utils import create_aiohttp_service
from models.cv_tensorflow.resnet import load_model, score_model

app = create_aiohttp_service(load_model, score_model)

if __name__ == '__main__':
    web.run_app(app)
