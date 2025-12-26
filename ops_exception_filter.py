import csv

INPUT_FILE = "transactions.csv"
OUTPUT_FILE = "exceptions.csv"

def is_exception(row):
    status = row["status"].strip().upper()
    error_code = row["error_code"].strip()

    if status in ["FAILED", "PENDING"]:
        return True
    if error_code:
        return True

    return False


with open(INPUT_FILE, newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

exceptions = [row for row in rows if is_exception(row)]

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(exceptions)

print(f"Processed {len(rows)} records")
print(f"Found {len(exceptions)} exception records")
