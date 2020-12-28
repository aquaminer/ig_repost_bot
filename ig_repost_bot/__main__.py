from time import sleep

from . import config
from .core import Core
from .utils import shared_storage


def main():
    print("Initializing the targets list")
    [Core.init_target(username) for username in config["ig_repost_bot"]["targets_usernames"]]

    print("Starting...")
    while True:
        for target in shared_storage.targets:
            print(
                f"@{target.username} (id: {target.id}) | feed: ", end=""
            )

            feed_count = Core.process_queue(
                target, shared_storage.api.user_feed(target.id)["items"], "feed"
            )
            print(f"{feed_count} new elements | stories: ", end="")

            stories_count = Core.process_queue(
                target, shared_storage.api.user_story_feed(target.id)["reel"]["items"], "stories"
            )
            print(f"{stories_count} new elements")
        sleep(60)


if __name__ == "__main__":
    main()
