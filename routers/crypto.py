from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()

templates = Jinja2Templates(directory="templates/")


@router.get('/crypto')
def list_coins(request: Request):
    return templates.TemplateResponse('list_crypto_coins.html', context={'request': request, 'output': ['BTC', 'ETH', 'XRP']})
