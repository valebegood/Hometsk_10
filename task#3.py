
from random import randrange
import csv 

summary = []
names = ('Mark', 'Mary', 'Josh', 'Kate', 'Luke')
for name in names:
    score = str(randrange(1000)) 
    summary.append({'Player name': name, 'Score': score})
    
with open('summary.csv', 'w', newline='', encoding='utf-8') as f:
    f_names = ['Player name','Score']
    writer = csv.DictWriter(f, fieldnames = f_names)

    writer.writeheader()
    
    for row in summary:
        writer.writerow(row)

    