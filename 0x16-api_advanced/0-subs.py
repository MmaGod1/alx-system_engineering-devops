#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    # Set up the URL with the subreddit name
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/your_username)"
    }

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is valid (status code 200)
    if response.status_code == 200:
        # Parse the response JSON and return the number of subscribers
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    else:
        return 0
