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
a=(input("a="))
b=(input("b="))
c=(input("c="))
d=(a+b+c)
print("a+b+c=",d)





