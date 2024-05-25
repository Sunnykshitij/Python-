#write a python program is multiple(n,m), that takes two integervalues and returen true if n is multiple of m, that n=mi
#returns true if n is multiple of m that n=mi for some integer i and otherwise false.
def mulfunc():
    n=int(input("n="))
    m=int(input("m="))
    if n%m==0:
        print("True")
    else:
        print("False")
mulfunc()