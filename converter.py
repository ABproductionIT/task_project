import main


class wdconv:
    units = {
        'kilogram': ('weight', 1.),
        'pound': ('weight', 0.453592),
        'meter': ('distance', 1.),
        'kilometer': ('distance', 1000.),
        'centimeter': ('distance', 0.01),
        'millimeter': ('distance', 0.001),
        'mile': ('distance', 1609.35),
        'feet': ('distance', 0.3048),
        'inch': ('distance', 0.0254),
        'B': ('data', 1),
        'KB': ('data', 1024),
        'MB': ('data', 1024.0**2),
        'GB': ('data', 1024.0**3),
        'TB': ('data', 1024.0**4),
        'PB': ('data', 1024.0**5)

    }

    def convert(self, param, in_param, out_param):
        main.Log_writer.write(self, ("convert "+str(param)+str(in_param)+" "+str((wdconv.units[in_param])[0])+" to "+str(out_param)))
        # write log example` user convert 1.0KB data to B
        return (param*(wdconv.units[in_param])[1])/(wdconv.units[out_param][1])


def ConvMenu(self):
    main.Log_writer.write(self, "open converter menu")
    print("-----What you are wont to convert?----\na. Data,\nb. Body Mass Index,\nc. Age,\nd. Lenght,\ne. Area,\nf. Discount\n")
    m = input("enter char of your choose\n")
    if m == "a":
        Dataconv(self)
    if m == "b":
        bmi(self)
    else:
        main.Menu.other_input(self, m, "converter.ConvMenu(self)")


def Dataconv(self):
    main.Log_writer.write(self, "open data converter")
    print("data converter is started!")
    valve = float(input("enter input valve"))
    print("Choose type of input valve \nByte B, Kilobyte KB, Megabyte MB, Gigabyte GB, Terabyte TB, Petabyte PB")
    indatatype = input("(Enter B,KB,MB,GB,TB or PB)")
    print("Choose type of output valve")
    outdatatype = input("(Enter B,KB,MB,GB,TB or PB)")
    main.Log_writer.write(self, ("wont convert "+str(valve)+str(indatatype)+" to "+str(outdatatype)+"`s"))
    result = wdconv.convert(self, valve, indatatype, outdatatype)
    print(valve, indatatype, " = ", result, outdatatype)
    main.Log_writer.write(self, ("convert result = "+str(result)))
    back = input("enter for go to converter menu")
    ConvMenu(self)


def bmi(self):
    main.Log_writer.write(self, "open  Body Mass Index converter")
    print("-- what do you wont to convert? --")
    print("1. Weight ??? Kilograms, Pounds\n2. Height ??? Centimeters, Meters, Feet, Inches")
    m = input()
    # menu
    if m == "1":
        main.Log_writer.write(self, "open weight converter")
        print("weight converter is started!")
        valve = float(input("enter input valve"))
        print("Choose type of input valve \n 'kilogram' or 'pound'")
        indatatype = input("(Enter - | ")
        if indatatype == "pound":
            outdatatype = "kilogram"
        if indatatype == "kilogram":
            outdatatype = "pound"
        print("converting ", valve, indatatype, " to ", outdatatype)
        result = wdconv.convert(self, valve, indatatype, outdatatype)
        print(valve, indatatype, " = ", result, outdatatype)
        ConvMenu(self)
    if m == "2":
        pass
