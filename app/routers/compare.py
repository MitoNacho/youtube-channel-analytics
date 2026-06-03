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

    error_message = None

    if "error" in first_channel:
        error_message = YoutubeService.error_message(
            first_channel["error"]
        )

    if "error" in second_channel:
        error_message = YoutubeService.error_message(
            second_channel["error"]
        )

    return templates.TemplateResponse(

        request=request,

        name="compare.html",

        context={

            "request": request,

            "first": first_channel,

            "second": second_channel,

            "error_message": error_message

        }

    )
