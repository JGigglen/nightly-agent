import requests
from datetime import datetime

SUBREDDITS = [
    "Entrepreneur",
    "startups",
    "SaaS",
    "SideProject",
    "SmallBusiness",
    "WebDev",
]

HEADERS = {"User-Agent": "nightly-agent/1.0"}

KEYWORDS = [
    "problem",
    "issue",
    "pain",
    "struggle",
    "annoying",
    "manual",
    "slow",
    "expensive",
    "need a tool",
    "looking for",
]

def fetch_posts(limit=25):
    posts = []
    for sub in SUBREDDITS:
        url = f"https://www.reddit.com/r/{sub}/new.json?limit={limit}"
        try:
            r = requests.get(url, headers=HEADERS, timeout=10)
            if r.status_code != 200:
                continue
            data = r.json()
            for item in data["data"]["children"]:
                p = item["data"]
                text = (p.get("title", "") + " " + p.get("selftext", "")).lower()
                score = sum(1 for kw in KEYWORDS if kw in text)
                if score > 0:
                    posts.append({
                        "subreddit": sub,
                        "title": p.get("title", ""),
                        "score": score,
                        "upvotes": p.get("score", 0),
                        "url": f"https://reddit.com{p.get('permalink','')}",
                    })
        except Exception:
            continue
    return posts

def run_idea_hunt():
    ideas = fetch_posts()
    ideas = sorted(
        ideas,
        key=lambda x: (x["score"], x["upvotes"]),
        reverse=True
    )
    return {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "ideas_found": len(ideas),
        "top_ideas": ideas[:10],
    }
