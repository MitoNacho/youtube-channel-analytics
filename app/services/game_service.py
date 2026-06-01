import random

from app.data.channels import BIG_CHANNELS
from app.data.channels import MEGA_CHANNELS
from app.data.channels import MID_CHANNELS
from app.services.youtube_service import YoutubeService


class GameService:

    CATEGORIES = [
        MID_CHANNELS,
        BIG_CHANNELS,
        MEGA_CHANNELS
    ]

    @staticmethod
    def create_round():
        # Keep pair selection grouped so both channels are comparable.
        category = random.choice(
            GameService.CATEGORIES
        )

        first_name, second_name = random.sample(
            category,
            2
        )

        first_channel = YoutubeService.search_channel(
            first_name
        )

        second_channel = YoutubeService.search_channel(
            second_name
        )

        return {
            "first": first_channel,
            "second": second_channel
        }

    @staticmethod
    def check_answer(first, second, choice):
        first_subs = int(
            first["subs_raw"]
        )

        second_subs = int(
            second["subs_raw"]
        )

        if first_subs == second_subs:
            return True

        winner = "first"

        if second_subs > first_subs:
            winner = "second"

        return choice == winner
