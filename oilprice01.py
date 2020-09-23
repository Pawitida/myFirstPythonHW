check = True
while check:
    print("#" * 80)
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 35 + "WELCOME" + " " * 36 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)
    i = input("Enter")

    print("#" * 80) #เลือกชนิดน้ำมัน
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 35 + "MENU OIL" + " " * 35 + "#")
    print("#" + " " * 23 + "1.Gasoline 95  Price 29.16 Baht" + " " * 24 + "#")
    print("#" + " " * 23 + "2.Gasoline 91  Price 25.30 Baht" + " " * 24 + "#")
    print("#" + " " * 23 + "3.Gasohol  91  Price 21.68 Baht" + " " * 24 + "#")
    print("#" + " " * 23 + "4.Gasohol E20  Price 20.2  Baht" + " " * 24 + "#")
    print("#" + " " * 23 + "5.Gasohol  95  Price 21.2  Baht" + " " * 24 + "#")
    print("#" + " " * 23 + "6.Diesel       Price 21.1  Baht" + " " * 24 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)
    s = input("Select oil 1-6 : ")

    print("#" * 80) #เลือกราคาเป็นลิตร หรือ ลิตรเป็นราคา
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 36 + "SELECT" + " " * 36 + "#")
    print("#" + " " * 31 + "1.price to liter" + " " * 31 + "#")
    print("#" + " " * 31 + "2.liter to price" + " " * 31 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)
    m = input("Select 1.price to liter or 2.liter to price : ")
    pricetoliter = "1"
    litertoprice = "2"
    if pricetoliter in m:
        l = int(input("price : "))
    elif litertoprice in m:
        l = int(input("liter : "))
    e = m.upper()
    b = 0
    if pricetoliter in m: #คำนวนราคาเป็นลิตร
        if "1" in e:
            b = b + (l / 29.16)
            print("oil", '%.2f' % b, "liter")
        elif "2" in e:
            b = b + (l / 25.30)
            print("oil", '%.2f' % b, "liter")
        elif "3" in e:
            b = b + (l / 21.68)
            print("oil", '%.2f' % b, "liter")
        elif "4" in e:
            b = b + (l / 20.2)
            print("oil", '%.2f' % b, "liter")
        elif "5" in e:
            b = b + (l / 21.2)
            print("oil", '%.2f' % b, "liter")
        elif "6" in e:
            b = b + (l / 21.1)
            print("oil", '%.2f' % b, "liter")
        else:
            print("Invalid information, plase Enter again")
    elif litertoprice in m: #คำนวนลิตรเป็นราคา
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

    print("#" * 80) #เลือกว่าจะออกจากเมนูหรือกลับไปที่เมนูใหม่
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 36 + "SELECT" + " " * 36 + "#")
    print("#" + " " * 30 + "1.Exit the program" + " " * 30 + "#")
    print("#" + " " * 31 + "2.Back the menu" + " " * 32 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)
    print("1.Exit the program or 2.back the menu")
    a = '0'
    while (a not in '12'):
        a = input()
        if (a == '1'):
            check = False
