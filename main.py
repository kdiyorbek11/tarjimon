x = int(input("1-sonni kiriting"))
y = int(input("2-sonni kiriting"))
z = int(input("3-sonni kiriting"))
o = x+y+z
print(o)



#2



x = ["azamat", "aziz", "kamol", "komil"]
for i in x:
    print(len(i))
print(x)


#3



t = [1,2,3,4,5,6,4,6,85,4,6,5,2,6,4,5,2,5,5,5,5,5,5,8,6,]
for i in t:
    if i % 2 == 0:
        print("juft sonlar" , i)



#4

p = ["aziza", "aziz", "kamol", "diyorbek"]
p.sort(reverse=True)
print(p)

#5



x = ["olimjon", "nozanin", "diyorbek"]
x.sort(reverse=True)
print(x)



#6

q = [1,2,3,4,5,6,4,6,85,4,6,5,2,6,4,5,2,5,5,5,5,5,5,8,6,]

w = list(set(q))
print(w)


#7

y = ["aziza", "aziz", "kamol", "diyorbek"]
print(len(y))

#8



k = [1,2,3,4,5,6,4,6,85,4,6,5,2,6,4,5,2,5,5,5,5,5,5,8,6,]
element = 99
if element in k:
    print(f"{element} ro`yxatda mavjud")
else:
    print(f"{element} ro`yxatda mavjud emas")




#9



x = ["aziza", "aziz", "kamol", "diyorbek"]
for i in enumerate(x):
    print(i)




#10


z = ["aziza", "aziz", "kamol", "diyorbek"]
x.remove("aziza")
print(x)