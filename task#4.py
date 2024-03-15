import csv

with open('summary.csv', 'r', encoding='utf8') as f:
    reader = csv.DictReader(f)
    reserv = list(reader)
    
for row in reserv:
    
    scores = row['Score'].strip('[]').split(', ')
    
    scores = [int(score) for score in scores]
    
    row['Score'] = max(scores)


revers = sorted(reserv, key=lambda x: x['Score'], reverse=True)


with open('new_summary.csv', 'w', encoding='utf8', newline='') as new_f:
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(new_f, fieldnames=fieldnames)
    writer.writeheader()
    for row in revers:
        writer.writerow(row)     