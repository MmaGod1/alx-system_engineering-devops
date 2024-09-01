#!/usr/bin/python3
"""
Calculates the number of subscribers
"""
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API and returns the number of subscribers for a given subreddit.
    If an invalid subreddit is given, return 0.
    """
    # Set up the URL and headers
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my_reddit_api'}

    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check the response status
    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
