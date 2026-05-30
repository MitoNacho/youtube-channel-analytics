from fastapi import APIRouter
from fastapi import Request

from fastapi.templating import Jinja2Templates

from app.services.youtube_service import YoutubeService

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/compare")
def compare_page(
    request: Request,
    first: str,
    second: str
):

    first_channel = YoutubeService.search_channel(
        first
    )

    second_channel = YoutubeService.search_channel(
        second
    )

    return templates.TemplateResponse(

        request=request,

        name="compare.html",

        context={

            "request": request,

            "first": first_channel,

            "second": second_channel

        }

    )