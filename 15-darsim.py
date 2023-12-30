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
for a in range(1,11):
    if b/a%2==0:
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
else:
    print("bo`linmaydi ")  

    
    








