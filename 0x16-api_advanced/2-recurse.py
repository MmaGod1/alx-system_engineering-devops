#!/usr/bin/python3
"""
2-recurse
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    Queries the Reddit API recursively to return a list of all hot articles
    for a given subreddit.
    If no results are found for the given subreddit, return None.
    """
    if hot_list is None:
        hot_list = []

    # Set up the URL and headers
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'my_reddit_api'}
    params = {'after': after}

    # Send a GET request to the Reddit API
    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
            )

    # Check if the request was successful and not a redirect
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data'].get('after')

        # Add the titles of the current page's posts to the list
        for post in posts:
            hot_list.append(post['data']['title'])

        # If there's more data, recurse to get the next page
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None
