from operator import itemgetter

from . import config
from .utils import *


class Core:
    @staticmethod
    def init_target(target_username: str) -> None:
        searched_users = shared_storage.api.search_users(target_username)["users"]
        for usr in searched_users:
            if usr["username"] != target_username:
                continue

            ret_target = Target(id=usr["pk"], username=target_username)
            shared_storage.targets.append(ret_target)
            break

    @staticmethod
    def process_queue(target: Target, results: list, timestamp_key: str) -> int:
        counter = 0  # New items counter

        results_sorted_by_timestamp = [
            x for x in reversed(sorted(results, key=itemgetter("taken_at")))
        ]  # Sort all items by "taken_at" key and then reverse it, so ...
        # it will be provided from the newest item to the oldest item

        if len(results) == 0:  # If there's nothing in feed
            if not target.latest_timestamp[timestamp_key]:
                target.latest_timestamp[timestamp_key] = 0
            return 0

        if not target.latest_timestamp[
            timestamp_key]:  # If latest timestamp isn't set yet, we'll set it to the newest item's timestamp
            target.latest_timestamp[timestamp_key] = results_sorted_by_timestamp[0][
                "taken_at"
            ]
            return 0

        new_timestamp = target.latest_timestamp[timestamp_key]
        for result in results_sorted_by_timestamp:
            if result["taken_at"] <= target.latest_timestamp[timestamp_key]:
                continue

            content_type = "Image" if result["media_type"] == 1 else "Video"  # Instagram and es3n1n being 100iq - FIXME

            url = Utils.get_biggest_image_size(
                result["image_versions2"]["candidates"]
                if content_type == "Image"
                else result["video_versions"]
            )
            caption = (
                result["caption"]["text"]
                if "caption" in result.keys()
                   and result["caption"] is not None
                   and "text" in result["caption"].keys()
                else None
            )
            if caption:
                caption = caption.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')  # Remove HTML chars

            body = f"{content_type} by {target.get_ig_tag()}"
            if caption not in [None, "", " "]:
                body = f"<code>{caption}</code> - (c) {target.get_ig_tag()}"

            if content_type == "Image":
                shared_storage.bot.send_photo(config["telegram"]["channel_id"], url, caption=body, parse_mode="HTML")
            else:
                shared_storage.bot.send_video(config["telegram"]["channel_id"], url, caption=body, parse_mode="HTML")

            new_timestamp = result["taken_at"]
            counter += 1
        target.latest_timestamp[timestamp_key] = new_timestamp

        return counter
