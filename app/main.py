import os

from fastapi import FastAPI
from fastapi import Request

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

from app.routers import channels
from app.routers import compare
from app.routers import game

app = FastAPI(
    title="Youtube Analytics API"
)

app.add_middleware(
    SessionMiddleware,
    secret_key=os.getenv("SESSION_SECRET_KEY", "youtube-analytics-dev-secret")
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="app/templates"
)

app.include_router(channels.router)
app.include_router(compare.router)
app.include_router(game.router)


@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(

        request=request,

        name="home.html",

        context={
            "request": request
        }

    )
