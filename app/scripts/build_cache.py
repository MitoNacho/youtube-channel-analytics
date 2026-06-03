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
                channel_names.append(channel_name)

    return channel_names


def build_cache():
    channels = {}
    errors = 0

    for channel_name in unique_channel_names():
        try:
            channel_data = YoutubeService.search_channel(channel_name)

            if "error" in channel_data:
                errors += 1
                print(f"Error en {channel_name}: {YoutubeService.error_message(channel_data['error'])}")
                continue

            # The game only needs identity, avatar, and subscriber data.
            channels[channel_name] = {
                "channel_id": channel_data["channel_id"],
                "name": channel_data["name"],
                "avatar": channel_data["avatar"],
                "subs": channel_data["subs"],
                "subs_raw": channel_data["subs_raw"]
            }

        except Exception as exc:
            errors += 1
            print(f"Error en {channel_name}: {exc}")

    cache_data = {
        "last_updated": date.today().isoformat(),
        "channels": channels
    }

    CACHE_PATH.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    CACHE_PATH.write_text(
        json.dumps(cache_data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print(f"Canales procesados: {len(channels)}")
    print(f"Canales con error: {errors}")

    return cache_data


if __name__ == "__main__":
    build_cache()
