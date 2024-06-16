# write a function which takes input as a parameter and return in words:
names={1:"one",2:"Two",3:"Three",4:"four",5:"five"}
num=int(input("The number:"))
if num<100:
    for num in names:
        k=names.get(num)
        print(num,"in words is",k)