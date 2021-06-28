#taking dimension of matrix
n=int(input())

#taking the matrix input
mat=[]
for i in range(n):
    l=list(map(int,input().split()))
    mat.append(l)

#below is the function

def diagsum(mat,n):
    primary=0
    secondary=0
    for i in range(n):
        primary+=mat[i][i]
        secondary+=mat[n-i-1][i]
    return primary,secondary


#calling the function

primary,secondary = diagsum(mat,n)

print("primary diagonal sum is = ", primary)
print("secondary diagonal sum is = ", secondary)
print("total sum is = ", primary+secondary)

