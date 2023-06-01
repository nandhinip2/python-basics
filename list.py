#list is used to put multiple values in a single variable
list1=[2,3,4,5,]
list2=["and","is"]
list3=[True,False]
print(list1)
print(list2)
print(list3)
#list is ordered,indexed,changable and allow duplicate values
list4=[5,6,7,5,6]
print(list4)
print(len(list4))
print(len(list1))
print(type(list1))
a=["one",1,"two",2,True,False]
print(a)
#list constructor
b=(2,3,4,5,6)
c=list((b))
print(c)
d=["bottle","bag","cap","pen","table","chair","lap"]
print(d[0])
print(d[-1])
print(d[1])
print(d[-2])
print(d[0:3])
print(d[2:7])
print(d[2:])
print(d[:5])
#range of negative index
print(d[-4:-1])
if "chair" in d:
    print("yes chair is in the list")
if "table" in d:
    print("yes table is in d")
#how to change item in a list
d[2]="cup"
print(d)
d[0:3]="window","door","ac"
print(d)
d[0:3]="paper","book","scale","eraser"
print(d)
d[4:9]="board","light","fan"
print(d)
d[2:4]=["white"]
print(d)
#insert item
d=['paper', 'book', 'white', 'board', 'light', 'fan']
d.insert(2,"phone")
print(d)
d.insert(1,"case")
print(d)
d.insert(4,"plug")
print(d)
#append item
d.append("bag")
print(d)
d.append("box")
d.append("ring")
print(d)
#extend
e=["file","edit","view","navigate"]
f=["code","refractor","run","tools"]
e.extend(f)
print(e)
g=["vcs","window"]
h=("basics","operators","problems")
g.extend(h)
print(g)
#remove items
g.pop(1)
print(g)
g.pop()
print(g)
# del g
# print(g)
del g[2]
print(g)
g.clear()
print(g)
#loop
h=["assignment","exams","project","report"]
for x in h:
    print(x)
#list comprehension
fruits=["apple","banana","kiwi"]
list5=[]
for x in fruits:
    if "a" in x:
        list5.append(x)
print(list5)
for x in fruits:
    if "i" in x:
        list5.append(x)
print(list5)
#sort
d=['Paper', 'book', 'white', 'board', 'light', 'fan']
d.sort()
print(d)
i=[3,5,7,8,4,]
i.sort()
print(i)
i.sort(reverse=True)
print(i)
d.sort(reverse=True)
print(d)
d.sort(key=str.lower)
print(d)
e=["file","edit","view","navigate"]
e.reverse()
print(e)
f=e.copy()
print(f)
f=list(e)
print(f)
g=(e+f)
print(g)
e=["file","edit","view","navigate"]
f=["file","edit","view","navigate"]
for x in f:
    e.append(x)
    print(e)
e.extend(f)
print(e)
a=max(e)
print(a)
b=max(i)
print(b)
k=[23356,324568,89965,34470770,3456667,567]
k.sort()
print(k)
print(k[2])

