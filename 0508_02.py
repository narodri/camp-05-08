n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

f=0

for i in range(n):
    if A[i]==B[i]:
        f=1
        print(i+1,end=" ")

if(f==0):
    print("0")