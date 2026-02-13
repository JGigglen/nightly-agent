from idea_hunt import run_idea_hunt

def main():
    print("[nightly-agent] Starting run")

    ideas = run_idea_hunt()

    print(f"[ideas] Found {ideas['ideas_found']} candidate ideas")
    for i, idea in enumerate(ideas["top_ideas"], 1):
        print(f"{i}. {idea['title']} ({idea['subreddit']})")

    print("[nightly-agent] Done")

if __name__ == "__main__":
    main()
