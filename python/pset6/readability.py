from cs50 import get_string

letters = 0
words = 1
sentences = 0

text = get_string("Text: ")

for i in range(len(text)):
    if text[i].isalpha():
        letters += 1
    if text[i].isspace():
        words += 1
    if text[i] == '.' or text[i] == '?' or text[i] == '!':
        sentences += 1

L = ((letters * 100.00) / words)
S = ((sentences * 100.00) / words)
index = 0.0588 * L - 0.296 * S - 15.8

if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print(f"Grade {round(index)}")