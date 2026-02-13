from datetime import datetime

def main():
    now = datetime.utcnow().isoformat()
    print(f"[nightly-agent] Ran at {now} UTC")

if __name__ == "__main__":
    main()
