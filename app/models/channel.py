channel_data = YoutubeService.search_channel(
    channel
)

videos = YoutubeService.recent_videos(
    channel_data["channel_id"]
)