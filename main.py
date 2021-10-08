import uvicorn

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates/")


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse('index.html', context={'request': request, 'output': 'Hello World'})


if __name__ == "__main__":
    uvicorn.run(app)
