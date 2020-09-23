#ดึงราคาน้ำมันจากเว็บ
from zeep import Client
from lxml import etree

client = Client('https://www.pttor.com/OilPrice.asmx?WSDL')
result = client.service.CurrentOilPrice(Language="en")
root = etree.fromstring(result)
n = len(root)
name = ['none']
price = [0]
for i in range(n):
    if len(root[i]) == 3:
        name.append(root[i][1].text)
        price.append(float(root[i][2].text))

check = True
while check:
    print("#" * 80) #เมนูหลัก
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
    for i in range(1, len(name)):
        print("#" + ' ' * 20 + name[i] + " has price: " + str(price[i]) + " baht" + " " * 20 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" + " " * 78 + "#")
    print("#" * 80)
    s = input("Select oil : ")

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
