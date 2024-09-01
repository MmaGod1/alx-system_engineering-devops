#!/usr/bin/python3
"""
100-count
"""

from collections import defaultdict
import re
import requests


def count_words(subreddit, word_list, hot_list=None, after=None):
    """
    Queries the Reddit API recursively to count occurrences of keywords
    in the titles of hot articles from a given subreddit.
    """
    if hot_list is None:
        hot_list = []

    # Set up the URL and headers
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my_reddit_api'}
    params = {'after': after}

    # Send a GET request to the Reddit API
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        after = data['data'].get('after')

        # Add the titles of the current page's posts to the list
        for post in posts:
            hot_list.append(post['data']['title'].lower())

        # If there's more data, recurse to get the next page
        if after:
            return count_words(subreddit, word_list, hot_list, after)
        else:
            # Count the occurrences of each keyword in the collected titles
            word_count = defaultdict(int)
            word_regex = {
                word: re.compile(
                    rf'\b{re.escape(word)}\b', re.IGNORECASE
                )
                for word in word_list
            }

            for title in hot_list:
                for word, pattern in word_regex.items():
                    word_count[word] += len(pattern.findall(title))

            # Sort results first by count (descending), then alphabetically
            sorted_counts = sorted(
                word_count.items(),
                key=lambda x: (-x[1], x[0])
            )

            # Print results
            for word, count in sorted_counts:
                print(f"{word}: {count}")

    else:
        # If the subreddit is invalid, print nothing
        return None
