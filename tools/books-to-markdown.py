"""
Tracking books in external tool with export capability to CSV. Import the CSV,
fix some issues, export as markdown table
"""
import csv
import os

header_printed = False
desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
csv_file = 'Books 2023.csv'
with open(os.path.join(desktop, csv_file), 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        if len(row) == 5:
            book, author, month, b_format, notes = row
        elif len(row) == 4:
            book, author, month, b_format = row
            notes = ""
        elif len(row) == 3:
            book, author, month = row
            b_format = ""
            notes = ""
        output_row = f"| {book} | {author} | {month} | {b_format} | {notes} |"
        print(output_row.replace("â€™", "'"))
        if not header_printed:
            print("| --- | --- | --- | --- | --- |")
            header_printed = True

