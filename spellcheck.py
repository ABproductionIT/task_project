import main
from spellchecker import SpellChecker

spell = SpellChecker()


def menu():
    print("1. Write text\n2. Open text file")
    nav = input()
    if nav == "1":
        text = input()
        editor(text)
    if nav == "2":
        url = input()
        open_file(url)


def editor(text):
    print(text)
    print("a. Check text, b. Save text")
    choose = input()
    if choose == "a":
        check(text)
    if choose == "b":
        save_file(text)


def check(text):
    words = text.split(sep=" ")
    listspellwords = []
    titlemaker = False
    for word in words:
        if word == "i":
            word = "I"
        listspellwords.append(word)
    listspellwords[0] = (listspellwords[0]).title()
    for i in range(len(listspellwords)):
        a = str(listspellwords[i][(len(listspellwords[i])-1)])
        if a == "?" or a == "!" or a == ".":
            try:
                listspellwords[i+1] = listspellwords[i+1].title()
            except:
                pass
    print(' '.join(listspellwords))


def open_file(url):
    with open(url) as file:
        text = file.read()
        editor(text)


def save_file():
    pass


menu()
