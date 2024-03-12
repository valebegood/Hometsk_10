any_content = 'Very short content'

with open('file.txt', 'w', encoding='utf8') as f:
    f.write(any_content)


with open('file.txt', 'r', encoding='utf8') as f:
    uppercase = f.read().upper()


with open('new_file.txt', 'w', encoding='utf8') as f:
    f.write(uppercase)    