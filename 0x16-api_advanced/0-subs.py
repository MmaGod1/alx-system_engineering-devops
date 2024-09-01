#!/usr/bin/python3
"Function to find out how many subscribers"
import requests

def number_of_subscribers(subreddit):
  """This function queries the Reddit API to get the number of subscribers for a given subreddit."""
  # Construct the API endpoint URL
  url = f"https://www.reddit.com/r/{subreddit}/about.json"
  headers = {"User-Agent": "MyCoolScript v1.0 (by /u/your_username)"}

  try:
    response = requests.get(url, allow_redirects=False, headers=headers)
    response.raise_for_status()
  except requests.exceptions.RequestException:
    return 0

  data = response.json()
  if not data.get("data"):
    return 0
  return data["data"].get("subscribers", 0)
