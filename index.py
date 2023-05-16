arr = input().split()
arr2=[]
for i in arr:
    if len(i)<4:
        arr2.append(i)
print(arr2)