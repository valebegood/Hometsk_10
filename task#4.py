import csv

with open('summary.csv', 'r', encoding='utf8') as f:
    reader = csv.DictReader(f)
    reserv = list(reader)
revers = sorted(reserv, key=lambda x: int(x['Score']), reverse=True)
with open('new_summary.csv', 'w', encoding='utf8', newline ='') as new_f:
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(new_f, fieldnames=reader.fieldnames)
    writer.writeheader()
    for row in revers:
            new_f.write(f"{row['Player name']}, {row['Score']}\n")
     