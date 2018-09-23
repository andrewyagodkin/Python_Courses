with open('text.txt', 'r', encoding='utf-8') as file:
    text=' '
    for line in file:
        text= text + line


text_save = text

text_len=len(text)
text = text.replace("\n", " ")
text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
words = text.split()
print('Кол-во слов: 'len(words))
print('Кол-во символов: 'len(text))

text_save = text_save.replace('.', '!')

with open('referat2.txt', 'w', encoding='utf-8') as file:
    file.write(text_save)