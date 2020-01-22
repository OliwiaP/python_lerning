print("hello world!")
a=10
b=7.5
c="cos"
d=[1,2,3]
f=(1,2,3)

print(a)
print(b)
print(str(a)+c)
print(str(type(d))+" "+str(type(f)))

d.append(c)

for i in d:
    print(i)

for i in range(len(d)):
    print(d[i])