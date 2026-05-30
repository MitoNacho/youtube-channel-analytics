from fastapi import FastAPI
from fastapi import Request

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routers import channels
from app.routers import compare

app = FastAPI(
    title="Youtube Analytics API"
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


@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(

        request=request,

        name="home.html",

        context={
            "request": request
        }

    )