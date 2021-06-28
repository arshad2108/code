
#recursive fucntion below
def recureven(i,x):
    if i>x:
        return
    print(i,end=" ")
    recureven(i+2,x)

#taking the x input
x=int(input())
recureven(0,x)
