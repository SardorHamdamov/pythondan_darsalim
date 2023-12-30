#murrakab shartli opertirlar
"""
yosh=(int(input("Yoshingizni kriting:\n 🤑")))  
if yosh<8:
    print("Sizga krish bepul😁")
elif yosh<13:
    print("sizga krish 5000so`m")
else:
    print("Sizga krish 10000so`m😎")
    """
"""
yosh=(int(input("Yoshingizni kriting:\n 🤑")))  
if yosh<8:
    narx=0
elif yosh<13:
    narx=5000
else:
    narx=10000
print(f"Sizga krish {narx} so`m ")
 """
"""
model=["labo","damas","nexia","gentra"]
print("fort" in model)
 """

"""
a=(input("Dam olish kunini kriting:\n"))
if a=="shanba" or a=="yakshanba":
    print("Dam olish kuni")
else:
    print("Yo`q dam olish kuni emas")
"""

"""
a=int(input("a="))
b=int(input("b="))
if (a>12) and (b>1):
    print("ikkala son xam togri")
else:
    print("boshqa sonlarni kriting")
"""
""""

son = input("1 dan 40 gacha bo'lgan sonlarni kiriting\n")
if son.isdigit():
    son = int(son)
    

    if son>0 and son<30:
        qoldiq =son % 10
        letter=""

        if son>9 and son<20:
            letter = "O'n "

        elif son>19 and son<30:
            letter="Yigirma "

        elif  son>29 and son<40:
            letter="o'tiz "

        if qoldiq==1:
            letter+="bir"

        elif qoldiq==2:
            letter +="Ikki"
            
        elif qoldiq==3:
            letter +="Uch"
            
        elif qoldiq==4:
            letter +="to'rt"

        elif qoldiq==5:
            letter +="besh"

        elif qoldiq==6:
            letter +="olti"

        elif qoldiq==7:
            letter +="yetti"

        elif qoldiq==8:
            letter += "sakkiz"

        elif qoldiq==9:
            letter +="toqqiz"

        print(letter)      
           
    else:
         print("1 dan 30 gacha bo'gan sonlarni kirting")
else:
    print("son kiriting")

"""












                  #1-mash
#kritilgan a soni musbat upki manfiy ekanliginin aniqlovchi dastur
"""

x=(int(input("Manfiy(-) yoki musbat(+) son kriting:\n")))
if 0>x:
    print("Tanlagan soniz manfiy",x)
else:
    print("Tanlagan soniz musbat",x)


                    #2-mashq
 #kritilgan son juft yoki toq ekanligini tekshiruvchi dastur😍
a=(int(input("Juft yoki toq son tanlang\n >>>")))
if a%2==0:
    print("Xa juft son👌")
else:
    print("Xa toq son👏")



                     #3-mashq
# #tomonlari a va b teng to`g`ri  to`rtburchak kvadrat ekanligini aniqlovchi dastur tuzing.
a=(int(input("a tomon uzunligini son bilan kriting:\n a=")))
b=(int(input("b tomon uzunligini son bilan kriting:\n b=")))
if a==b:
    print("Tomonlari teng to`g`ri  to`rtburchak ")
else:
    print("Tomonlari teng emas to`g`ri  to`rtburchak")



                      #4-mashq
# #kritilgan a soni to`rt honali son ekanligini aniqlovchi dastur tuzing
a=(int(input("To'rt honali son kriting\n >>>")))
if a>999 and a<10000:
    print("Siz kritgan son to'rt xonali son ",a)

else:
    print("Afsuski siz kritgan son to'rt xonali son emas")
"""

                  #5-mashq
#ikki xonali sonning raqamlari toq ekanligini aniqlovchi dastur 
x=(int(input("Ikki xonali toq son tanlang\n >>>")))
if x%2==0:
    print(x,"=","Ikki xonali toq son emas buu. 👌")
elif x>100:
    print(x,"=","Ikki xonali toq son emas.🤦‍♂️")
elif x<10:
    print(x,"=","Ikki xonali toq son kriting.😒")
else:
    print(x,"=","Xa ikki xonali  toq son.✔")

                  #6-mashq
#uch xonali sonda bir xil raqamlar mavjudligini tekshiruvchi dastur.
"""
x=(int(input("Brinchi sondi kriting:\n")))
y=(int(input("Ikkinchi sondi kriting:\n")))
z=(int(input("Uchinchi sondi kriting:\n")))
if x==y==z:
    print("Siz chiroyli raqamingiz",x,y,z)
else:
    print("Siz shartni to`liq bajarmadigiz",x,y,z)
"""

                 #7-mashq
#a va b sondan qaysi biri juft ekanligini aniqlovchi dastur
"""
a=(int(input("Brinchi sondi kriting:\n a=")))
b=(int(input("Ikkinchi sondi kriting:\n b=")))
if a%2==0:
   print("xa juft son",a)
elif b%2==0:
   print("xa juft son",b)
else:
   print("juft son emas")
"""

                 #8-mashq
#3ta butun son krting. Qaysi biri juft ekanligini aniqlovchi dastur
"""   

a=(int(input("Brinchi sondi kriting:\n a=")))
b=(int(input("Ikkinchi sondi kriting:\n b=")))
d=(int(input("Ucinchi sondi kriting:\n a=")))

if a%2==0:
   print("xa juft son",a)
elif b%2==0:
   print("xa juft son",b)
elif d%2==0:
   print("xa juft son",d)
else:
   print("juft son emas")
"""   


"""

a=int(input("To'rt honali son kriting\n >>>"))
if (a>1000) and (a==1000):
    print("Siz kritgan son to'rt xonali son  ",a)
elif a<10000:
    print("Afsuski siz kritgan son to'rt xonali son emas")
else:
    print("Afsuski siz kritgan son to'rt xonali son emas")
"""












