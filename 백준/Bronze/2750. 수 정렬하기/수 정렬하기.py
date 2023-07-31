n = int(input())
l = [int(input()) for _ in range(n)]
# print(l)
for i in range(n):
    for j in range(i+1,n):
        if l[i]>l[j]:
            c = l[i]
            l[i] = l[j]
            l[j] = c
# print(l)
l = [str(i) for i in l]
print('\n'.join(l))