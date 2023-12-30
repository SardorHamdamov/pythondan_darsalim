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


x={"g","b","i","f"}
y={"a","c","d","e"}
x.issuperset(y)
print(x)







