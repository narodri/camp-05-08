n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

out=[0,0]

for j in range(len(arr)):
    if j%4==0:
        out[1]+=arr[j]
    elif j%4==1:
        out[0]+=arr[j]
    elif j%4==2:
        out[1]-=arr[j]
    else:
        out[0]-=arr[j]

print(out[0],out[1])