from datetime import datetime
from datetime import timezone


def time_ago(date_string):

    published_date = datetime.strptime(
        date_string,
        "%Y-%m-%dT%H:%M:%SZ"
    )

    published_date = published_date.replace(
        tzinfo=timezone.utc
    )

    now = datetime.now(
        timezone.utc
    )

    difference = now - published_date

    days = difference.days

    if days > 0:

        if days == 1:
            return "1 day ago"

        return f"{days} days ago"

    hours = difference.seconds // 3600

    if hours > 0:

        if hours == 1:
            return "1 hour ago"

        return f"{hours} hours ago"

    minutes = difference.seconds // 60

    if minutes > 0:

        if minutes == 1:
            return "1 minute ago"

        return f"{minutes} minutes ago"

    return "Just now"