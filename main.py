import requests

# Public ad-block list (hosts format)
BLOCK_LIST_URL = "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts"

blocked_domains = []

print("Downloading ad block list...")

response = requests.get(BLOCK_LIST_URL)
lines = response.text.splitlines()

for line in lines:
    if line.startswith("0.0.0.0"):
        domain = line.split()[-1]
        blocked_domains.append(domain)

print(f"Total domains blocked: {len(blocked_domains)}")

# Save results
with open("blocked_domains.txt", "w") as f:
    for domain in blocked_domains[:100]:  # limit for simplicity
        f.write(domain + "\n")

print("Sample blocked domains saved to blocked_domains.txt")
