from aiohttp import web
from models.sentiment_xgboost.pipeline import TextSelector, NumberSelector, Tokenizer
from services.utils.aiohttp_service_utils import create_aiohttp_service
from models.sentiment_xgboost.model import load_model, score_model

app = create_aiohttp_service(load_model, score_model)

if __name__ == '__main__':
    web.run_app(app)
