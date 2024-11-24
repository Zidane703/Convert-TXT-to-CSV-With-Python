# Read a TXT file and write its content to a CSV
import csv

with open("Testing.txt", "r") as txt_file:
    with open("Testing.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        for line in txt_file:
            cleaned_line = line.strip()  # Remove leading/trailing spaces or newlines
            writer.writerow([cleaned_line])
