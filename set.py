#set is used to store multiple items in asingle variable
#it is not indexed, orderd ,it is unchnagable and donot allow duplicates
a={1,2,3,4,5}
print(a)
x={"day","night","summer","winter","spring"}
print(x)
r={1,0,3,5,"jan","feb","march",True,False}
print(r)
#here trye and 1 ,false and 0 are considered  the same
print(len(x))
print(type(x))
s=("april","may","june")
w=set(s)
print(w)
for x in s:
    print(x)
print("april" in s)
print("june" not in s)
z={"july"}
w.add("july")
print(w)
p={"august","september","oct"}
w.update(p)
print(w)
o={"k","j","v","o"}
f=["d","e","i"]
o.update(f)
print(o)
#remove
o.remove("d")
print(o)
o.pop()
print(o)
o.discard("k")
print(o)
o.clear()
print(o)
# del o
# print(o)
w={"up","down"}
x={"left","right"}
z=(w.union(x))
print(z)
h={"add","sub"}
j={"multiply","div","add"}
v=h.intersection(j)
print(v)
i=h.symmetric_difference(j)
print(i)


