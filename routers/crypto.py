from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix='/crypto')

templates = Jinja2Templates(directory="templates/")


@router.get('/')
def list_coins(request: Request):
    return templates.TemplateResponse('list_crypto_coins.html', context={'request': request, 'output': ['BTC', 'ETH', 'XRP']})
