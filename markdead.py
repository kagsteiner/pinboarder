
import os
import pinboard
import requests
from dotenv import load_dotenv

load_dotenv()

PINBOARD_TOKEN = os.getenv("PINBOARD_TOKEN")

if not PINBOARD_TOKEN:
    print("Error: PINBOARD_TOKEN not found in .env file.")
    exit(1)

pb = pinboard.Pinboard(PINBOARD_TOKEN)

def is_dead(url):
    """Checks if a URL is dead.

    Returns:
        tuple[bool, str | None]: A tuple containing a boolean indicating if the site is dead,
                                 and a string with the reason if it is.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "en-US,en;q=0.9",
    }
    try:
        response = requests.get(url, timeout=10, headers=headers)
        if response.status_code >= 400 and response.status_code != 403:
            return True, f"HTTP status code {response.status_code}"
        return False, None
    except requests.exceptions.RequestException as e:
        return True, f"Request failed: {e}"


def main():
    """Main function to check and tag dead bookmarks."""
    print("Fetching all bookmarks...")
    all_posts = pb.posts.all()
    print(f"Found {len(all_posts)} bookmarks.")

    dead_bookmarks = []
    for post in all_posts:
        dead, reason = is_dead(post.url)
        if dead:
            print(f"  - Found dead link: {post.url} ({reason})")
            dead_bookmarks.append(post)

    if not dead_bookmarks:
        print("No dead bookmarks found.")
        return

    print(f"Found {len(dead_bookmarks)} dead bookmarks.")
    for post in dead_bookmarks:
        if "dead" not in post.tags:
            print(f"Tagging {post.url} with dead")
            post.tags.append("dead")
            pb.posts.add(
                url=post.url,
                description=post.description or post.url,
                extended=post.extended,
                tags=post.tags,
                shared=post.shared,
                toread=post.toread,
            )
        else:
            print(f"{post.url} is already tagged with dead")


if __name__ == "__main__":
    main()
