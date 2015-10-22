# Python Json loops
def total_ups():
    children = json.loads(reddit_front)["data"]["children"]
    return sum(c["data"]["ups"] for c in children)
