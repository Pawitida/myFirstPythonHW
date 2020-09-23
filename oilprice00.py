check = True
while check:
    print("********************************************************************************")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                     MENU OIL                                 *")
    print("*                         1.Gasoline 95  Price 29.16 Baht                      *")
    print("*                         2.Gasoline 91  Price 25.30 Baht                      *")
    print("*                         3.Gasohol  91  Price 21.68 Baht                      *")
    print("*                         4.Gasohol E20  Price 20.2  Baht                      *")
    print("*                         5.Gasohol  95  Price 21.2  Baht                      *")
    print("*                         6.Diesel       Price 21.1  Baht                      *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("*                                                                              *")
    print("********************************************************************************")
    s = input("Select oil 1-6 : ")
    m = input("Select 1.price to liter or 2.liter to price : ")
    pricetoliter = "1"
    litertoprice = "2"
    if pricetoliter in m:
        l = int(input("price : "))
    elif litertoprice in m:
        l = int(input("liter : "))
    e = m.upper()
    b = 0
    if pricetoliter in m:
        if "1" in e:
            b = b + (l/29.16)
            print("oil", '%.2f' %b, "liter")
        elif "2" in e:
            b = b + (l/25.30)
            print("oil", '%.2f' %b, "liter")
        elif "3" in e:
            b = b + (l/21.68)
            print("oil", '%.2f' %b, "liter")
        elif "4" in e:
            b = b + (l/20.2)
            print("oil", '%.2f' %b, "liter")
        elif "5" in e:
            b = b + (l/21.2)
            print("oil", '%.2f' %b, "liter")
        elif "6" in e:
            b = b + (l/21.1)
            print("oil", '%.2f' %b, "liter")
        else:
            print("Invalid information, plase Enter again")
    elif litertoprice in m:
        if "1" in e:
            b = b + (l * 29.16)
            print("price", b, "Baht")
        elif "2" in e:
            b = b + (l * 25.30)
            print("price", b, "Baht")
        elif "3" in e:
            b = b + (l * 21.68)
            print("price", b, "Baht")
        elif "4" in e:
            b = b + (l * 20.2)
            print("price", b, "Baht")
        elif "5" in e:
            b = b + (l * 21.2)
            print("price", b, "Baht")
        elif "6" in e:
            b = b + (l * 21.1)
            print("price", b, "Baht")
        else:
            print("Invalid information, plase Enter again")
    else:
        print("plase Enter again")
    #while True:
    print("1.Exit or 2.back the menu : ")
    a = '0'
    while (a not in '12'):
        a = input()
        if (a == '1') :
            check = False
