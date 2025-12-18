print("Website Blocker Simulation – GitHub Run")

sites = ["facebook.com", "youtube.com", "gmail.com"]

with open("data/hosts_simulated.txt", "w") as f:
    for site in sites:
        f.write(f"127.0.0.1 {site}\n")
        print(f"Blocked: {site}")

print("Simulation completed")
