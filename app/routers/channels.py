from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

from app.services.youtube_service import YoutubeService

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/channel/{name}")
def channel(name: str):

    channel_data = YoutubeService.search_channel(
        name
    )

    videos = YoutubeService.recent_videos(
        channel_data["channel_id"]
    )

    return {

        "channel": channel_data,

        "recent_videos": videos

    }


@router.get("/search")
def search_channel(
    request: Request,
    channel: str
):

    channel_data = YoutubeService.search_channel(
        channel
    )

    videos = YoutubeService.recent_videos(
        channel_data["channel_id"]
    )

    return templates.TemplateResponse(

        request=request,

        name="channel.html",

        context={

            "request": request,

            "channel": channel_data,

            "videos": videos

        }

    )