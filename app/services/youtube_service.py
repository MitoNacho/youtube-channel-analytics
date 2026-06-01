import os
import requests

from app.utils.date_formatter import time_ago
from app.utils.formatters import format_number
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

BASE_URL = "https://www.googleapis.com/youtube/v3"


class YoutubeService:

    @staticmethod
    def search_channel(channel_name):

        print("API KEY:")
        print(API_KEY)

        url = f"{BASE_URL}/search"

        params = {

            "part": "snippet",
            "q": channel_name,
            "type": "channel",
            "key": API_KEY

        }

        response = requests.get(
            url,
            params=params
        )

        data = response.json()

        print("STATUS CODE:")
        print(response.status_code)

        print("RESPONSE DATA:")
        print(data)

        if "items" not in data:

            return {
                "error": data
            }

        if len(data["items"]) == 0:

            return {
                "error": "No channels found"
            }

        channel_id = data["items"][0]["id"]["channelId"]

        return YoutubeService.get_channel_stats(
            channel_id
        )

    @staticmethod
    def get_channel_stats(channel_id):

        url = f"{BASE_URL}/channels"

        params = {

            "part": "snippet,statistics",
            "id": channel_id,
            "key": API_KEY

        }

        response = requests.get(
            url,
            params=params
        )

        data = response.json()

        print("CHANNEL DATA:")
        print(data)

        if "items" not in data:

            return {
                "error": data
            }

        if len(data["items"]) == 0:

            return {
                "error": "Channel not found"
            }

        item = data["items"][0]

        subs_raw = int(
            item["statistics"].get("subscriberCount", 0)
        )

        views_raw = int(
            item["statistics"].get("viewCount", 0)
        )

        videos_raw = int(
            item["statistics"].get("videoCount", 0)
        )

        return {

            "channel_id": channel_id,

            "name":
            item["snippet"]["title"],

            "avatar":
            item["snippet"]["thumbnails"]["high"]["url"],

            "subs":
            format_number(subs_raw),

            "subs_raw":
            subs_raw,

            "views":
            format_number(views_raw),

            "views_raw":
            views_raw,

            "videos":
            format_number(videos_raw),

            "videos_raw":
            videos_raw

                }

    @staticmethod
    def recent_videos(channel_id):

        url = f"{BASE_URL}/search"

        params = {
            "part": "snippet",
            "channelId": channel_id,
            "maxResults": 6,
            "order": "date",
            "type": "video",
            "key": API_KEY
        }

        response = requests.get(
            url,
            params=params
        )

        data = response.json()

        videos = []

        if "items" not in data:
            return videos

        for video in data["items"]:

            videos.append({
                "title": video["snippet"]["title"],
                "date": time_ago(video["snippet"]["publishTime"]),
                "thumbnail": video["snippet"]["thumbnails"]["high"]["url"],
                "video_id": video["id"]["videoId"]
            })

        return videos
