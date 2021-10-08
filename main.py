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
async def root(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request, 'output': 'Hello World'})


@app.get("/hello")
@app.get("/hello/{name}")
async def hello(request: Request, name: str = 'World'):
    return templates.TemplateResponse('index.html', context={'request': request, 'output': f'Hello {name}'})


if __name__ == "__main__":
    uvicorn.run(app)
