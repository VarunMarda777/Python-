import csv

INPUT_FILE = "transactions.csv"
EXCEPTIONS_FILE = "exceptions.csv"
SUMMARY_FILE = "summary.txt"

def is_exception(row):
    status = row["status"].strip().upper()
    error_code = row["error_code"].strip()
    return status in ["FAILED", "PENDING"] or bool(error_code)

total = 0
failed = 0
pending = 0
error = 0
exceptions = []

with open(INPUT_FILE, newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    rows = list(reader)

for row in rows:
    total += 1
    status = row["status"].strip().upper()
    error_code = row["error_code"].strip()

    if status == "FAILED":
        failed += 1
    if status == "PENDING":
        pending += 1
    if error_code:
        error += 1

    if is_exception(row):
        exceptions.append(row)

with open(EXCEPTIONS_FILE, "w", newline="", encoding="utf-8") as exfile:
    writer = csv.DictWriter(exfile, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(exceptions)

with open(SUMMARY_FILE, "w", encoding="utf-8") as sfile:
    sfile.write(f"Total transactions: {total}\n")
    sfile.write(f"Exception transactions: {len(exceptions)}\n")
    sfile.write(f"Failed transactions: {failed}\n")
    sfile.write(f"Pending transactions: {pending}\n")
    sfile.write(f"Transactions with errors: {error}\n")

print("Ops reports generated successfully")
