import main


def ConvMenu(self):
    main.Log_writer.write(self, "open converter menu")
    print("What you are wont to convert?\na. Data,\nb. Body Mass Index,\nc. Age,\nd. Lenght,\ne. Area,\nf. Discount\n")
    m = input("enter char of your choose\n")
    if m == "a":
        Dataconv(self)
    if m == "b":
        bmi(self)


def Dataconv(self):
    main.Log_writer.write(self, "open data converter")
    print("data converter is started!")
    valve = float(input("enter input valve"))
    print("Choose type of input valve \nByte B, Kilobyte KB, Megabyte MB, Gigabyte GB, Terabyte TB, Petabyte PB")
    indatatype = input("(Enter B,KB,MB,GB,TB or PB)")
    print("Choose type of output valve")
    outdatatype = input("(Enter B,KB,MB,GB,TB or PB)")
    main.Log_writer.write(self, ("wont convert "+str(valve)+str(indatatype)+" to "+str(outdatatype)+"`s"))
    print(formatFileSize(valve, indatatype, outdatatype))
    main.Log_writer.write(self, ("convert result = "+str(formatFileSize(valve, indatatype, outdatatype))))
    ConvMenu(self)



def convertFloatToDecimal(f=0.0, precision=2):
    '''
    Convert a float to string of decimal.
    precision: by default 2.
    If no arg provided, return "0.00".
    '''
    return ("%." + str(precision) + "f") % f


def formatFileSize(size, sizeIn, sizeOut):
    '''
    Convert file size to a string representing its value in B, KB, MB and GB.
    The convention is based on sizeIn as original unit and sizeOut
    as final unit.
    '''
    assert sizeIn.upper() in {"B", "KB", "MB", "GB", "TB", "PB"}, "sizeIn type error"
    assert sizeOut.upper() in {"B", "KB", "MB", "GB", "TB", "PB"}, "sizeOut type error"
    if sizeIn == "B":
        if sizeOut == "KB":
            return convertFloatToDecimal((size/1024.0))
        elif sizeOut == "MB":
            return convertFloatToDecimal((size/1024.0**2))
        elif sizeOut == "GB":
            return convertFloatToDecimal((size/1024.0**3))
        elif sizeOut == "TB":
            return convertFloatToDecimal((size/1024.0**4))
        elif sizeOut == "PB":
            return convertFloatToDecimal((size/1024.0**5))
    elif sizeIn == "KB":
        if sizeOut == "B":
            return convertFloatToDecimal((size*1024.0))
        elif sizeOut == "MB":
            return convertFloatToDecimal((size/1024.0))
        elif sizeOut == "GB":
            return convertFloatToDecimal((size/1024.0**2))
        elif sizeOut == "TB":
            return convertFloatToDecimal((size/1024.0**3))
        elif sizeOut == "PB":
            return convertFloatToDecimal((size/1024.0**4))
    elif sizeIn == "MB":
        if sizeOut == "B":
            return convertFloatToDecimal((size*1024.0**2))
        elif sizeOut == "KB":
            return convertFloatToDecimal((size*1024.0))
        elif sizeOut == "GB":
            return convertFloatToDecimal((size/1024.0))
        elif sizeOut == "TB":
            return convertFloatToDecimal((size/1024.0**2))
        elif sizeOut == "PB":
            return convertFloatToDecimal((size/1024.0**3))
    elif sizeIn == "GB":
        if sizeOut == "B":
            return convertFloatToDecimal((size*1024.0**3))
        elif sizeOut == "KB":
            return convertFloatToDecimal((size*1024.0**2))
        elif sizeOut == "MB":
            return convertFloatToDecimal((size*1024.0))
        elif sizeOut == "TB":
            return convertFloatToDecimal((size/1024.0))
        elif sizeOut == "PB":
            return convertFloatToDecimal((size/1024.0**2))
    elif sizeIn == "TB":
        if sizeOut == "B":
            return convertFloatToDecimal((size*1024.0**4))
        elif sizeOut == "KB":
            return convertFloatToDecimal((size*1024.0**3))
        elif sizeOut == "MB":
            return convertFloatToDecimal((size*1024.0**2))
        elif sizeOut == "GB":
            return convertFloatToDecimal((size*1024.0))
        elif sizeOut == "PB":
            return convertFloatToDecimal((size/1024.0))
    elif sizeIn == "PB":
        if sizeOut == "B":
            return convertFloatToDecimal((size*1024.0**5))
        elif sizeOut == "KB":
            return convertFloatToDecimal((size*1024.0**4))
        elif sizeOut == "MB":
            return convertFloatToDecimal((size*1024.0**3))
        elif sizeOut == "GB":
            return convertFloatToDecimal((size*1024.0**2))
        elif sizeOut == "TB":
            return convertFloatToDecimal((size*1024.0))


def bmi(self):
    main.Log_writer.write(self, "open  Body Mass Index converter")
    print("-- what do you wont to convert? --")
    print("1. Weight – Kilograms, Pounds\n2. Height – Centimeters, Meters, Feet, Inches")
    m = input()
    # menu
    if m == "1":
        amt = 1
        wdconv.convert(amt, 'kg', 'pound')
    if m == "2":
        pass

class wdconv:
    units = {
        'kg': ('weight', 1.),
        'kilo': ('weight', 1.),
        'kilogram': ('weight', 1.),
        'lb': ('weight', 2.204),
        'pound': ('weight', 2.204),
        'tonne': ('weight', 0.001),
        'carat': ('weight', 5000.),
        'gram': ('weight', 1000.),
        'dram': ('weight', 564.4),
        'ounce': ('weight', 35.27),
        'grain': ('weight', 15430.),
        'm': ('distance', 1.),
        'meter': ('distance', 1.),
        'kilometer': ('distance', 0.001),
        'km': ('distance', 0.001),
        'centimeter': ('distance', 100.),
        'cm': ('distance', 100.),
        'meter': ('distance', 1.),
        'mile': ('distance', 0.0006214),
        'chain': ('distance', 0.04971),
        'furlong': ('distance', 0.004971),
        'league': ('distance', 0.0002071),
        'foot': ('distance', 3.281),
        'feet': ('distance', 3.281),  # irregular plural - must be explicitly specified!
        'inch': ('distance', 39.37)
    }
