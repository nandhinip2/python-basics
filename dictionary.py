#used to save data in key-value pairs
a={"school":"vasavi","college":"vasavi","school":"kv"}
print(a)
# it is indexed,ordered,changable,do not allow duplicates
print(len(a))
print(type(a))
print(a["school"])
print(a.get("college"))
print(a.keys())
print(a.values())
a["college"]="sc"
print(a)
print(a.items())
a["city"]="pkd"
print(a)
if "city" in a:
    print("it is in a")
print("city" in a)
a.update({"school":"st raphels"})
print(a)
a.update({"dist":"pkd"})
print(a)
a.pop("school")
print(a)
a.popitem()
print(a)
del a["city"]
print(a)
a.clear()
print(a)
# del a
#print(a)
a={"school":"vasavi","college":"vasavi","school":"kv"}
for x,y in a.items():
    print(x,y)
for x in a.keys():
    print(x)
for y in a.values():
    print(y)
b=a.copy()
print(b)
c=dict(a)
print(c)
#nested dict
school={"class1":{"a":1,"b":2},"class2":{"c":1,"d":3}}
print(school)
class1={"s":7,"f":9}
class2={"x":3,"l":8}
class3={"Z":1,"g":6}
school={"class1":class1,"class2":class2,"class3":class3}
print(school)



