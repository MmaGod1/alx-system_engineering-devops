#!/usr/bin/python3
"""Print hot posts on a given Reddit subreddit."""
import requests

def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit."""
    
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(None)
        return
    
    try:
        data = response.json()
        if 'data' not in data or 'children' not in data['data']:
            print(None)
            return
        
        posts = data['data']['children']
        if not posts:
            print(None)
            return
        
        for post in posts[:10]:
            print(post['data']['title'])
    except (ValueError, KeyError):
        print(None)
