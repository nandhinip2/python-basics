a=("a","w","e","p","h")
print(a)
#use open brackets for tupples
#tupples is used to store multiple values in a single variable
#it is indexed,ordered and allows duplicates but is not changable
print(len(a))
print(type(a))
b=(1,2,3,"now","not",True,False)
print(b)
#tuple constructor
s=(2,45,67,8,9)
tuple(s)
print(s)
print(s[2])
print(s[-2])
print(s[0:3])
print(s[-5:-1])
if "now" in b:
    print("now is in b")
d=list(b)
print(d)
k=("english","hindi","malayalam","maths","physics")
a=list(k)
a[1:2]="chemistry","zoology","botany"
d=tuple(a)
print(d)
a.pop(3)
f=tuple(a)
print(f)
a.append("economics")
h=tuple(a)
print(h)
#loop
a=("kerala","karnataka","andra","maharashtra")
for x in a:
    print(x)
b=("jammu","punjab","gujarat")
c=(a+b)
print(c)
d=(b*2)
print(d)
e=d.count("jammu")
print(e)











