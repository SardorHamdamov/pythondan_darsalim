       #           1-dars
"""kocha="bogbon"
mahalla="sog`bon"
tuman="bodomzor"
viloyat="Samarqand"
print(kocha,mahalla,tuman,viloyat)

x="bogbon kochasi","Sog`bon mahallasi","Bodomzor tumani","Samarqan viloyati"
print(x)


x=("bogbon kochasi, Sog`bon mahallasi,Bodomzor tumani, Samarqan viloyati")


if input("yashash hududingizni kriting\n") in x:
   print("ha bor")
   
else:
	print("afsuski yuq")

x=("bogbon kochasi, Sog`bon mahallasi,Bodomzor tumani, Samarqan viloyati")

print(x)
print(x.upper())#Katta harflarda yozish
print(x.lower())#Kichik harflarda yozadi
print(x.title())
print(x.capitalize())


x=("bogbon kochasi", "Sog`bon mahallasi,Bodomzor tumani, Samarqan viloyati")
for y in x:
	print(y)
"""
"""x=int(input("istalgan sondi kiritin>>>"))
a=(x**2)
b=(x**3)
print(x,"ning kvadrati", a ,"ga teng")
print(x,"ning kubi", b ,"ga teng")
"""
"""

x=int(input("birinchi sondi kriting:"))
y=int(input("ikkinchi sondi kriting:"))
d=x+y
e=x-y
print("x*y=",x*y)
print("x/y=",x/y)
print("x+y=",d)
print("x-y=",e)
"""
                  


               #   3-dars


#3 dars
#paythonda operatorlari bilan ishlash


#arfimetik operatori

#x+y qoshish
#x-y ayrish
#x*y kopaytrish
#x/y bolish
#x**y darajaga kotaradi
#x//y butun sonni oladi
"""p=int(input("p="))
s=int(input("s="))
print("p+s=",p+s)
"""
"""g=int(input("g="))
h=int(input("h="))
print("g*h=",g*h)
"""
"""p=int(input("p="))
s=int(input("s="))
print("p-s=",p-s)
"""
"""p=int(input("p="))
s=int(input("s="))
print("p/s=",p/s)
"""
"""p=int(input("p="))
s=int(input("s="))
print("p**s=",p**s)
"""
"""p=int(input("p="))
s=int(input("s="))
print("p//s=",p//s)
"""



#ozlashtrish operatori

"""p=int(input("p="))
p+=55
print(p)
"""

"""p=int(input('P='))

p-=50
print('p=',p)
"""

"""p=int(input("p="))
p*=50
print('p=',p)
"""

"""p=int(input("p="))
p%=50
print("p=",p)
"""

"""p=int(input("p="))
p//=50
print("p=",p)
"""

#taqqoslash operatori

"""x>y
x<y
x>=y
x<=y
x==y
"""


"""p=int(input("p="))
if p<10:
    print("yuq 10 dan kichik")
else:
    print("xa 10 dan kotta")
"""


"""p=int(input("p="))
if p>10:
    print("xa 10 dan kotta")
else:
    print("yuq 10 dan kichik")
   """

"""
p=int(input("p="))
if p<10:
    print("yuq 10dan kichik")

elif p==10:
    print("xa 10 ga teng")
    
else:
    print("xa 10 dan katta")

"""

#mantiq operatori


"""x=int(input("x="))
print(x>5 and x<5)
"""

"""x=int(input("x="))
print(x<5 or x>5)
"""

"""x=int(input("x="))
print(not x<8 and x>23)
"""

#aniqlash operatorlari

"""p=["behi","o`rik"]

t=["behi","o`rik"]
s=p
p=s
print(p is t)
print(p is s)
print(p==s)
"""


#bitli operatorlar
"""&(and)
|(or)
^(xor)
~(not)
"""
"""x=int(input("x="))
print(x<6 | ~x>8)
"""



                #4-dars




#paythonda malumot turlari bilan ishlash


"""#1-mashq malumot turini aniqlash
x=int(3) #int butun turdagi malumot turi hisoblanadi
p=float(5.8)
s=str("satr korinshda")
y=list(["list","korinishda"])
print("x=3 >>",type(x))
print("p=5.8 >>>", type (p))
print("s=satr korinishida >>>", type(s))
print("y=[list,korinishda]>>>", type(y))
"""


#2-mashq pythonda sonlar int,float,complex


"""a=9
b=5.9
d=7j
print(type(a))
print(type(b))
print(type(d))
"""


#butun sonlar int;


"""x=int(input("x="))
print(bin(x)) #onlik sanoq sistemasiga otkaziw
print(x.bit_length())
"""


#xaqiqiy sonlar float;


"""x=6.678
print(type(x))
"""


"""x=(14.7).is_integer()
print(x)

x= (12.0).as_integer_ratio()
print(x)
"""


#complex sonlar


"""a=6+4j
b=7+3j
print(type (a+b)) #tipini aniqlaydi 'type' 
"""


"""a=4+5j
b=6+4j
print(a+b)
"""


"""a=5+2j
b=9+4j
print(a*b)
"""


"""a=complex(3,4)#complex(butun son+j)
b=complex(5,9)
print(a+b)
"""



#sonlarni ogrish
"""a=float(34)
b=2.0
print(a/b)
"""

"""a=int(56.2)

print(a)
"""

"""a="satr"
b=str(67)
print(a+b)
"""
#tasodifiy sonlar
"""

import random
print(random.randrange(1,1000))
"""


                   #5-dars




#print('paythonda satrlar bn iwlaw')


"""ism=input("ism=")
familya=input("familya=")
print(ism)
print(familya)"""

#satr bu massiv


"""a="qalesan"
print(a[-3])
"""
"""a="qalesan"
print(a[3])
"""
"""a="olma"
b="behi"
print(len(3*b+4*a))     #yegindisini xisoblaydi
"""

#matndi qirqib oladi


"""a="Sherzodbek"
print(a[0:4])
print(a[1:4])
print(a[2:4])
print(a[3:4])
print(a[4:4])
"""

"""a="Sherzodbek"
print(a[3:-2])
print(a[3:-4])
print(a[-5:-2])
print(a[-2:])
print(a[::-1]) #matndi teskari yozadi
"""

"""a="Salom qalesan"
print(a.upper()) #kotta harflarda yoziw
print (a.lower,()) #kichik harfda yoziw
"""

"""a="Chiroyli"
b="Dunyoyim"
print(a,b.replace("y","salom")) #shu matndagi harflarni orniga matn qoyish
print(
"""


#satrlarni tekshrish


"""txt="Man oqishga borishm kerak darsni tezroq tugating"
a="m" in txt     #matn ichidan matn qidradi
print(a)
"""

#satrlar formati

"""yow=25
matn="mening yoshim {} da"
print(matn.format(yow))
"""

#maxcuc belgilar

"""

a=input("a=")
print("\t",a)
"""



                    #6-dars



#list() royhatlar bn iwlash
"""meva=list(["shftoli","banan","gilos"])
print(meva)
print(type(meva))
"""


#elementlar murojat qilish
"""meva=("shftoli","banan","gilos","anor")
print(meva[-1])
print(meva[1])
print(meva[1:-1])
print(meva[1:])
"""


#elementlar qiymatini ozgartrish
"""meva=("shftoli","banan","gilos","anor")
print(meva)
meva[-1]="uzum" #royhatdagi mevani ozgartrish un
print(meva)
"""


"""meva=("shftoli","banan","gilos","anor")
for sardor in meva:
	print(sardor)
"""


#element mavjudligini tekwiriw


"""meva=["shaftoli","banan","gilos","anor"]
if input("mevani tanlang\n") in meva:
	print("ha bor")
else:
	print("tugab qolgan")
"""

	
#royhat uzunligini hisoblaw


#meva=["shaftoli","banan","gilos","anor"]
#print(meva)
#meva.append("nok") #qowiw
#meva.insert(0,"uzum") #orasiga qowiw
#meva.remove("banan") #orasidan del
#print(meva)
#meva.pop(-1)
#print(meva)
#del meva[3]
#print(meva)
#meva.clear() #uchrib tashledi
#meva2=meva.copy()
#meva2=list(meva)
#print(meva2,meva)


"""a=(1,2,3,4,5)
b=(6,7,8,9) #shunchaki 1ta satrga qowadi
print(a+b)
"""


"""a=[1,2,3,4,5]
b=[6,7,8,9]
for x in a:
    b.append(a)
print(b)
"""




               #7-dars






#royhatlar
"""meva=["uzum","gilos","banan","anor"]
x=[4,3,2,1,0]
meva.sort()
x.sort() #alfabit boyicha saralaw
print(meva)
print(x)"""

"""meva=["uzum","gilos","banan","anor"]
x=[4,3,2,1,0]
meva.reverse() #teskari royhat
print(meva)
print(x)
"""

#tuple(kartej)
"""x=["mers","audio","chevralet","ferari"]
y=("mers","audio","chevralet","ferari")
z=set(("mers","audio","chevralet","ferari"))
print(x,type(x))
print(y,type(y))
print(z,type(z))
"""
#elementlarga murojat
"""x=("mers","audio","chevralet","ferari")
print(x[1:2])

x=list("mers","audio","chevralet","ferari")
y=str(("mers","audio","chevralet","ferari"))
z=set(("mers","audio","chevralet","ferari"))
print(x)
print(y)
print(z)

x=("mers","audio","chevralet","ferari")
for x in x:
	print(x)


x=("mers","audio","chevralet","ferari")
if input("mahsulotni kiriting\n") in x:
	print("xa shunday mashina bor")
else:
    print("afsuski bunday mashina yuq")

#element qoshish

x=("mers","audio","chevralet","ferari")
y=("damas","gentra","malibu")
print(x*2+y)

toq_sonlar=(1,3,5,7,9,11,13,15,17,19,3,3)
juft_sonlar=(2,6,8,10,12,14,16,4,4)
a=toq_sonlar.count(3)
b=juft_sonlar.index(4)

print(a)
print(b)
"""
"""
x=(1,4,7,9,120,1,10,12,2,3,44,5)
print(x,"eng kotta son",max(x))
print(x,"eng kichik son",min(x))
print(x,"matndi uzunligi",len(x))
"""

"""

a=(input("a="))
b=(input("b="))
c=(input("c="))
d=(a+b+c)
print("a+b+c=",d)

"""





                #8-dars

#toplam sonlar


"""son={1,2,3,4,5,6}
print(son,type(son))
print(len(son)) #nechta elementdan iborat
"""


"""son={5,7,3,6,2,8,4,9}
for x in son:
	print(x)
print(1 in son)
"""


#elementlarni qo`shish


"""
son={5,7,3,6,2,8,4,9}
meva={"banan","nok","gilos"}
son.add(1) #ketma ket yozadi
meva.add("shaftoli")
son.update([3,14])
meva.update({"anor","uzum"})
print(son)
print(meva)
"""


#elementlarni o`chrish


"""
son={5,7,6,2,8,4,9} 
son.remove(2) #royhatdan o`chiradi
son.discard(5) #royhatdan o`chiradi
print(son)
"""


"""
meva={"banan","nok","gilos","nok"}
#meva.remove("nok")
meva.discard(3)
print(meva)
"""

#elementlarni tozalash clear()


"""
son={5,7,3,6,2,8,4,9}
son.clear() #tozalash yuq qilish
print(son)
"""

"""
son1={1,3,5,5,7,9}
son2={2,4,6,8,8,10}
son3=son1.union(son2) #tartib bn qowiw
print(son3)
"""


#nusxa oliw

"""
son1={1,3,5,5,7,9}
son2=son1.copy()
print(son2)
"""


#toplamlarni muhim funkisiyalar
#difference() difference_update()


"""
x={"a","b","d","f"}
y={"a","c","d","e"}
z=x.difference(y) #toplamlar ayrmasi
print(z)
"""

"""
x={"a","b","d","f"}
y={"a","c","d","e"}
x.difference_update(y) #toplamlar ayrmasi 
print(x)
"""


#intersection() intersection_update()


"""
x={"a","b","d","f"}
y={"a","c","d","e"}
z=x.intersection(y) #toplamlar kesishmasi 2lasida borini
print(z)
"""

"""
x={"a","b","d","f"}
y={"a","c","d","e"}
x.intersection_update(y) #toplamlar kesishmasi 2lasida borini
print(x)
"""


#isdisjoint()

"""
x={"g","b","i","f"}
y={"a","c","d","e"}
z=x.isdisjoint(y) #rost yolgon
print(z)
"""

#issubset(),issuperset()

"""
x={"a","b"}
y={"a","b"}
z=x.issubset(y)
print(z)
"""

"""
x={"g","b","i","f"}
y={"a","c","d","e"}
x.issuperset(y)
print(x)
"""



                #9-dars




#print("Sikl operatorlari")
#for ()
#1-mashq


"""mashinalar={"coblt","damas","isuzu","daf"}
for x in mashinalar:
	print(x)
"""

 #              2-mashq
"""
mashinalar={"coblt","damas","isuzu","daf"}
for x in mashinalar:
	print(f"bugun bizga {mashinalar}korgazmasi bolib otadi")
"""

#               3-mashq
#for yordamida sonli ro'yhatlar bilan ishlash

"""
son=list(range(1,11))
for x in son:
	print(f" {x} ning kvadradi {pow(x,2)} ga teng")
print(x)
"""



#           4-mashq
"""
mashina=[]
print("3ta yoqtrgan mashinagizni kriting\n")
for n in range(3):
    mashina.append(input(f"{n+1}-yoqtirgan mashinagizni nomini kriting\n"))
print("sizning yoqtrganmashinangiz",mashina)
"""

"""

son=[]
print("savol\n")
for b in range(4):
    son.append(input(f"{b+1}=javob berish="))
print(son,"javob bor")
"""




                #10-dars



#print("shartli operatorlar")
#if agar
#elif agar akas holda
#else aksa holad

""""
a=(input("a="))
b=(input("b="))
if a>b:
    print("ha a b dan kotta👏")
elif a==b:
    print("a b ga teng😊")
else:
    print("a b dan kichik🤦‍♂️")
    """
""""
a=float(input("a="))
b=float(input("b="))
c=print(f"{a}-{b}=",(a-b))
"""
""""
a=int(input("a="))
b=int(input("b="))
c=print(f"{a}+{b}=",(a+b))
"""
""""
til=input("uzb/eng tanlang\n")
if til=="uzb":
    print("hayrli kun")
elif til=="eng":
    print("my comon")
else:
    print("siz uzb yoki eng tanlang")
"""
""""
from random import randint
a=randint(1,50)
b=randint(1,50)
c=int(input("{}+{}=".format(a,b)))
if c==(a+b) :
    print("barakalla togri topdingiz")
else:
    print("natogri")
    """
""""
a=(int(input("a=")))
b=(float(input("b=")))
if a/b:
    print("ha")
"""

""""
x=int(input("yilni kriting:"))
#=(x//4)
c=print(x//4)

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))

d=(b**2-4*a*c)
if d>0:
    print("2ta yechimga ega ")

elif d==0:
    x1=(-b)/(2*a)
    print("1ta yechimga ega")
    print("x1=",x1)
else:
    print("yechimga ega emas")
"""
"""

a = int(input("yilni kiriting\n"))
if a%4==0:
    print("ha kamissa yili")
else:
    print("Kamissa yili emas")
"""







             #11-dars





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
"""

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




                   #12-dars




#for uchun takrorlanuchi 
"""
for a in range(1,11):
    print(a)
"""
"""

a=int(input("a="))
for b in range(1,11):
    natija=(a*b)
    print(f"{a} {"x"} {b} = {natija}")
"""
"""

for a in range(1,32,2):
    print(a)
print("kotta boling")

#3-mashq 

a=int(input("a="))
son=0
for n in range(1,a+1):
    if n%2==0:
        son=son+n
        print(n)
print("Juft sonlar yegindisi",son)        


from random import randint
a=[130,132,135]
b=randint(125,137)
i=0
while b in a:
    i+=1
    b=randint(125,137)
print("takrorlanishlar soni=",i)
print(b)

print("Kvadratni hisiblovchi dastur")

#x="istalgan sonni kriting dasturni to`xtatish uchun 'exit' so`zini yozing\n"
qiymat=''
while qiymat !='exit':
    qiymat=input("istalgan sonni kriting dasturni to`xtatish uchun 'exit' so`zini yozing\n")
    if qiymat !='exit':
        print(float(qiymat)**2)
print("raxmat")
"""
"""

a=int(input("a="))
c=int(a**1/2)+1
if 
    print("tub son",c)
else:
    print("tub son emas",c)

"""






                   #14-dars
                   






"""

oquvchi= {
    "ismi":"Mo`binaxon",
    "familyasi":"Raxmatalivna",
    "millati":"o`zbek",
    "tel_raqam":"yo`q"}
for a in oquvchi:
    print(f"kaliti {a} ga teng, Qiymati {oquvchi[a]} ha teng")

"""

"""

cars1={
    "model":"mers",
    "yil":2015
}
cars2={
    "model":"bmv",
    "yil":2013
}
cars3={
    "model":"nexia",
    "yil":2019
}
cars4={
    "model":"koblt",
    "yil":"2023"
}
cars={
    "cars1":cars1,
    "cars2":cars2,
    "cars3":cars3,
    "cars4":cars4
}
for a in cars.items():
    print(a)
"""


"""

talaba={
    "ismi":"Sardor",
    "familyasi":"Hamdamov",
    "yili":2001,
    "mllati":"o`zbek"
}
x=talaba.setdefault('talaba',"Yodgorek")
print(talaba,x)
"""





                   #15-dars
                   




"""

print("yoshni hisoblab beruvchi dastur")


def yow_krt(ism,yil):
    print(f"{ism} {2023-yil} yoshda")
yow_krt(ism=input("Ismingizni kriting:\n"),yil=int(input("Tugulgan yilingizni kritibng:\n")))


print("kvadratga kubga kotaruchi dastur")

print("Kirgizgan x,y sonini kvadratdga, kubga ko`tarib beramiz")
def hisobla(x,y):
    print(f"{x} soninig kvadrati {x**2} ga teng\n"
          f"{y} sonining kubi {x**3} ga teng\n")
hisobla(x=int(input("Hohlagan sondi kriting:x=\n")),y=int(input("Hohlagan sondi kriting:y=\n")))


print("sondi juft yoki toq ekanligini aniqlovchi dastur")


def juf_toq(a):
    if a%2==0 or a==0:
        print("Siz tanlagan son 'Juft' songa kiradi")
    else:
        print("Siz tanlagan son'Toq' songa kiradi")
        
juf_toq(a=int(input("Hohlagan sonizni kriting va bu 'Juft' yoki 'Toq' ekanini aniqlab beradi:\n")))


print("sondi kottasini aniqlab beradi")
print( "Hohlagan ikkita sonizni kriting va biz sizga kottasini aniqlab beramiz ")
def kotta_kichik(a,b):
    if a<b:
        print("Siz yozgan sonlar ichida kottasi",b)
    elif a>b:
        print(f"Siz yozgan sonlar ichida kottasi {a}")
    elif a==b:
        print(f"Siz yozgan sonlar teng {a}={b}")
        
kotta_kichik(a=input("a="),b=input("b="))


print(" x ning y chi darajasi") 
print("Hohlagan 'x' qiymatini kriting va biz sizga 'y' chi darajaga ko`tarib beramiz")
def hisobla(x,y):
    print(f"{x} sonining {y}-darajasi  {x**y} ga teng\n")
hisobla(x=int(input("Hohlagan sondi kriting :\n")),y=int(input("hohlagan sondi kriting:\n")))


print(" x ning kvadrati")


def hisobla(x):
    print(f"{x} sonining {2}-darajasi  {x**2} ga teng\n")
hisobla(x=int(input("Hohlagan sondi kriting va biz sizga kvadratga ko`tarib beramiz:\n")))

print("qoldiqsiz bolish")
"""



b=int(input("Hohlagan sondi kriting kritgan soniz bo`linish alomatini tekshirib beramiz=>>>"))
for a in range(1,15):
    
    if  b/a%2==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    elif b/a%3==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    elif  b/a%4==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    elif  b/a%5==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    elif  b/a%6==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    elif  b/a%7==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    elif  b/a%8==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    elif  b/a%8==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    elif  b/a%9==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    elif  a/b%10==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    elif  a/b%11==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    elif  a/b%12==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    elif  a/b%13==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    elif  a/b%14==0:
        print(f"{b} soni {a} ga qoldiqsiz bo`linad 'Natija'>>{b/a}")
    
    
  
"""


    



son = input("1 dan 40 gacha bo'lgan sonlarni kiriting\n")
if son.isdigit():
    son = int(son)
    

    if son>0 and son<41:
        qoldiq =son % 10
        letter=""

        if son>9 and son<20:
            letter = "O'n "

        elif son>19 and son<30:
            letter = "Yigirma "

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











































































































































































































































































