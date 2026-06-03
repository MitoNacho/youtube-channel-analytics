from fastapi import APIRouter
from fastapi import Request
from fastapi.templating import Jinja2Templates

from app.services.game_service import GameService

router = APIRouter()

templates = Jinja2Templates(
    directory="app/templates"
)


@router.get("/game")
def game_page(request: Request):

    round_data = GameService.create_round()

    if "error" in round_data:

        return templates.TemplateResponse(

            request=request,

            name="game.html",

            context={

                "request": request,

                "first": None,

                "second": None,

                "streak": request.session.get("streak", 0),

                "result": None,

                "error_message": round_data["error"]

            }

        )

    return templates.TemplateResponse(

        request=request,

        name="game.html",

        context={

            "request": request,

            "first": round_data["first"],

            "second": round_data["second"],

            "streak": request.session.get("streak", 0),

            "result": None,

            "error_message": None

        }

    )


@router.post("/game/check")
async def check_game(request: Request):

    form = await request.form()

    first = {
        "channel_id": form["first_channel_id"],
        "name": form["first_name"],
        "avatar": form["first_avatar"],
        "subs": form["first_subs"],
        "subs_raw": int(form["first_subs_raw"])
    }

    second = {
        "channel_id": form["second_channel_id"],
        "name": form["second_name"],
        "avatar": form["second_avatar"],
        "subs": form["second_subs"],
        "subs_raw": int(form["second_subs_raw"])
    }

    is_correct = GameService.check_answer(
        first,
        second,
        form["choice"]
    )

    current_streak = request.session.get("streak", 0)
    final_streak = current_streak

    if is_correct:
        request.session["streak"] = current_streak + 1
        final_streak = request.session["streak"]
        result = "correct"

    else:
        # Preserve the achieved streak for the result screen before resetting.
        final_streak = current_streak
        request.session["streak"] = 0
        result = "wrong"

    return templates.TemplateResponse(

        request=request,

        name="game.html",

        context={

            "request": request,

            "first": first,

            "second": second,

            "streak": request.session.get("streak", 0),

            "final_streak": final_streak,

            "result": result,

            "error_message": None

        }

    )
