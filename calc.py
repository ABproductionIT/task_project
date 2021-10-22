import main


def calculate(self, a, b, c):
    if c == "+":
        main.Log_writer.write(self, (str(a)+str(c)+str(b)))
        a = a + b
        print(a)
        main.Log_writer.write(self, ("="+str(a)))
        e = input("Choose method + - * /")
    if c == "-":
        main.Log_writer.write(self, (str(a)+str(c)+str(b)))
        a = a - b
        print(a)
        main.Log_writer.write(self, ("="+str(a)))
        e = input("Choose method + - * /")
    if c == "*":
        main.Log_writer.write(self, (str(a)+str(c)+str(b)))
        a = a * b
        print(a)
        main.Log_writer.write(self, ("="+str(a)))
        e = input("Choose method + - * /")
    if c == "/":
        main.Log_writer.write(self, (str(a)+str(c)+str(b)))
        a = a / b
        print(a)
        main.Log_writer.write(self, ("="+str(a)))
        e = input("Choose method + - * /")
    if e == "+" or "-" or "*" or "/":
        c = e
        b = float(input("Enter digit"))
        calculate(self, a, b, c)


def calcstarter(self):
    print("calculator is started")
    a = int(input("Enter dight "))
    c = input("Choose method '+','-','*','/'")
    b = float(input("Enter digit"))
    calculate(self, a, b, c)

