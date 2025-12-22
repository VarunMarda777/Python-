from urllib.request import urlopen
from datetime import datetime

# Public ad-block list (hosts format)
BLOCK_LIST_URL = "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"


def main():
    print("🚀 Project execution started")
    print(f"🕒 Start time: {datetime.now()}")

    blocked_domains = []

    print("⬇️ Downloading ad block list...")

    with urlopen(BLOCK_LIST_URL) as response:
        lines = response.read().decode("utf-8").splitlines()

    for line in lines:
        if line.startswith("0.0.0.0"):
            domain = line.split()[-1]
            blocked_domains.append(domain)

    print(f"📊 Total domains blocked: {len(blocked_domains)}")

    # Save sample results
    with open("blocked_domains.txt", "w") as f:
        for domain in blocked_domains[:100]:
            f.write(domain + "\n")

    print("💾 Sample blocked domains saved to blocked_domains.txt")
    print(f"🏁 End time: {datetime.now()}")
    print("🎉 Project completed successfully")


if __name__ == "__main__":
    main()
