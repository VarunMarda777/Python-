# Simulated Website Blocker (GitHub-safe)
import json
import logging


hosts_path = "data/hosts_simulated.txt"
redirect_ip = "127.0.0.1"
logging.basicConfig(
    filename="logs/blocker.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def load_config():
    with open("config/settings.json", "r") as file:
        return json.load(file)

def block_websites(websites):
    with open(hosts_path, "r+") as file:
        content = file.read()
        for site in websites:
            if site not in content:
                file.write(f"\n{redirect_ip} {site}")
                logging.info(f"Blocked {site}")

def unblock_websites(websites):
    with open(hosts_path, "r+") as file:
        lines = file.readlines()
        file.seek(0)

        for line in lines:
            if not any(site in line for site in websites):
                file.write(line)

        file.truncate()
        for site in websites:
            logging.info(f"Unblocked {site}")

        
if __name__ == "__main__":
   config = load_config()
    websites = config["websites"]

    block_websites(websites)
    print("Websites blocked (simulation).")

    # Uncomment below line to unblock
    # unblock_websites(websites)
