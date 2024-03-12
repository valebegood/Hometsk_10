from random import randrange
import string 

summary_text = []
alphabet = string.ascii_uppercase 
for i,letter in enumerate(alphabet, start=1):
  filename = f'{letter}.txt'
  with open(filename, 'w', encoding='utf-8') as f:
    text = str(randrange(100))
    summary_text.append((filename,text))
    summary = str(summary_text)
    f.write(text)

with open('summary.txt', 'w', encoding= 'utf-8' ) as f:
       for filename, text in summary_text:
           f.write(f'{filename}: {text}\n')
       