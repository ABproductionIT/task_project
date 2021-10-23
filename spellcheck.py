import main


def menu(self):
    main.Log_writer.write(self, "open Spell checker menu")
    print("1. Write text\n2. Open text file")
    nav = input("Enter your choose|>")
    if nav == "1":
        main.Log_writer.write(self, "choose write text")
        text = input("Enter text|>")
        main.Log_writer.write(self, ("write |>"+text))
        editor(text)
    if nav == "2":
        main.Log_writer.write(self, "choose Open text file")
        url = input("Enter url to txt file (text.txt)|>")
        main.Log_writer.write(self, ("enter url |> "+url))
        print("---File is open---")
        open_file(self, url)
    else:
        print("choose not found, try again")
        menu(self)


def editor(text):
    print(text)
    print("a. Check text, b. Save text")
    choose = input("Enter your choose |> ")
    if choose == "a":
        check(text)
    if choose == "b":
        save_file(text)
    else:
        print("Check again!")
        editor(text)


def check(text):
    words = text.split(sep=" ")
    listspellwords = []
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
    print("___text checked!!____")
    text = ' '.join(listspellwords)
    editor(text)


def open_file(self, url):
    with open(url) as file:
        main.Log_writer.write(self, ("open file"+url))
        text = file.read()
        editor(text)


def save_file(text):
    direct = input("Enter name, to save|>")
    with open(direct, "w") as outfile:
        outfile.write(text)
    editor(text)
