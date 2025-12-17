# Simulated Website Blocker (GitHub-safe)

hosts_path = "data/hosts_simulated.txt"
redirect_ip = "127.0.0.1"

def block_websites(websites):
    with open(hosts_path, "r+") as file:
        content = file.read()
        for site in websites:
            if site not in content:
                file.write(f"\n{redirect_ip} {site}")

if __name__ == "__main__":
    websites = ["facebook.com", "youtube.com"]
    block_websites(websites)
    print("Simulation completed. Websites blocked.")
