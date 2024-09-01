#!/usr/bin/python3
"""
1-top_ten
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    If not a valid subreddit, prints None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'my_reddit_api'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful and not a redirect
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        # Print the titles of the first 10 posts
        for i in range(min(10, len(posts))):
            print(posts[i]['data']['title'])
    else:
        print(None)
