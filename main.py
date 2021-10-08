import uvicorn

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from routers import crypto

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates/")

app.include_router(crypto.router)


@app.get("/")
async def index(request: Request):
    ipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et ' \
            'dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ' \
            'ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore ' \
            'eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia ' \
            'deserunt mollit anim id est laborum'
    return templates.TemplateResponse('index.html', context={'request': request, 'output': ipsum})


@app.get("/hello")
@app.get("/hello/{name}")
async def hello(request: Request, name: str = 'World'):
    return templates.TemplateResponse('index.html', context={'request': request, 'output': f'Hello {name}'})


if __name__ == "__main__":
    uvicorn.run(app)
