import json
import sys
from datetime import date
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.data.channels import BIG_CHANNELS
from app.data.channels import MEGA_CHANNELS
from app.data.channels import MID_CHANNELS
from app.services.youtube_service import YoutubeService

CACHE_PATH = PROJECT_ROOT / "app" / "cache" / "channels.json"

CHANNEL_GROUPS = (
    MEGA_CHANNELS,
    BIG_CHANNELS,
    MID_CHANNELS
)


def unique_channel_names():

    channel_names = []

    for group in CHANNEL_GROUPS:

        for channel_name in group:

            if channel_name not in channel_names:
                channel_names.append(
                    channel_name
                )

    return channel_names


def build_cache():

    errors = 0

    # Cargar caché existente

    channels = {}

    if CACHE_PATH.exists():

        try:

            existing_cache = json.loads(
                CACHE_PATH.read_text(
                    encoding="utf-8"
                )
            )

            channels = existing_cache.get(
                "channels",
                {}
            )

            print(
                f"Canales ya cacheados: {len(channels)}"
            )

        except Exception:

            channels = {}

    added_channels = 0

    for channel_name in unique_channel_names():

        # Saltar canales ya cacheados

        if channel_name in channels:

            print(
                f"Ya existe: {channel_name}"
            )

            continue

        try:

            print(
                f"Consultando: {channel_name}"
            )

            channel_data = YoutubeService.search_channel(
                channel_name
            )

            if "error" in channel_data:

                errors += 1

                print(
                    f"Error en {channel_name}: "
                    f"{YoutubeService.error_message(channel_data['error'])}"
                )

                continue

            channels[channel_name] = {

                "channel_id":
                channel_data["channel_id"],

                "name":
                channel_data["name"],

                "avatar":
                channel_data["avatar"],

                "subs":
                channel_data["subs"],

                "subs_raw":
                channel_data["subs_raw"]

            }

            added_channels += 1

        except Exception as exc:

            errors += 1

            print(
                f"Error en {channel_name}: {exc}"
            )

    cache_data = {

        "last_updated":
        date.today().isoformat(),

        "channels":
        channels

    }

    CACHE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    CACHE_PATH.write_text(

        json.dumps(
            cache_data,
            ensure_ascii=False,
            indent=2
        ),

        encoding="utf-8"

    )

    print()
    print("===== RESUMEN =====")
    print(f"Canales nuevos añadidos: {added_channels}")
    print(f"Canales con error: {errors}")
    print(f"Total en caché: {len(channels)}")
    print("===================")

    return cache_data


if __name__ == "__main__":

    build_cache()