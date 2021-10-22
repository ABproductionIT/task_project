import json
from datetime import datetime
import calc
import converter


class User:
    def user(self):
        if self is True:
            name = input("enter user name=")
            surname = input("enter user surname=")
            age = input("age=")
            gender = input("gender =")
            user_data_dict = {
              "login_date": str(datetime.now()),
              "username": name,
              "surname": surname,
              "age": age,
              "gender": gender}
            return User.user_data(user_data_dict), Menu.gird(self)

    def user_data(data):
        with open("user_data.json", "w") as outfile:
            json.dump(data, outfile)


class Menu:
    def gird(self):
        Log_writer.write(self, "open main menu")
        print("Menu\n Chose Tool for start the work\n1. Calculator\n2. Converter")
        chose = input("Enter number of Tool  ")
        if chose == "1":
            Log_writer.write(self, "choose calculator")
            calc.calcstarter(self)
        if chose == "2":
            Log_writer.write(self, "choose converter")
            converter.ConvMenu(self)


class Log_writer:
    def write(self, log):
        with open('user_data.json', 'r') as f:
            text = json.load(f)
            with open("user.log", "a") as logfile:
                 line = str(datetime.now())+" "+text['username']+" "+log
                 logfile.write(line + '\n')


if __name__ == '__main__':
    app = User.user(self=True)
