import json
import random
from pathlib import Path

from app.data.channels import BIG_CHANNELS
from app.data.channels import MEGA_CHANNELS
from app.data.channels import MID_CHANNELS

CACHE_PATH = (
    Path(__file__).resolve().parents[1]
    / "cache"
    / "channels.json"
)


class GameService:

    CATEGORIES = [
        MID_CHANNELS,
        BIG_CHANNELS,
        MEGA_CHANNELS
    ]

    @staticmethod
    def cache_exists():

        if not CACHE_PATH.exists():
            return False

        try:

            with CACHE_PATH.open(
                encoding="utf-8"
            ) as cache_file:

                cache_data = json.load(
                    cache_file
                )

            # JSON vacío
            if not cache_data:
                return False

            # No existe la clave channels
            if "channels" not in cache_data:
                return False

            # Existe pero está vacío
            if len(
                cache_data["channels"]
            ) == 0:
                return False

            return True

        except (
            json.JSONDecodeError,
            OSError
        ):

            return False

    @staticmethod
    def load_cache():

        with CACHE_PATH.open(
            encoding="utf-8"
        ) as cache_file:

            cache_data = json.load(
                cache_file
            )

        return cache_data.get(
            "channels",
            {}
        )

    @staticmethod
    def create_round():

        try:

            cache = GameService.load_cache()

        except FileNotFoundError:

            return {
                "error": "Game cache not found"
            }

        except json.JSONDecodeError:

            return {
                "error": "Game cache is not valid"
            }

        for _ in range(10):

            category = random.choice(
                GameService.CATEGORIES
            )




            valid_channels = [

            channel

            for channel in category

            if channel in cache

        ]

            if len(valid_channels) < 2:
                continue

            first_name, second_name = random.sample(
                valid_channels,
            2
        )

            return {

            "first":
            cache[first_name],

            "second":
            cache[second_name]

        }

        return {

        "error":
        "Not enough cached channels available"

    }

    @staticmethod
    def check_answer(
        first,
        second,
        choice
    ):

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