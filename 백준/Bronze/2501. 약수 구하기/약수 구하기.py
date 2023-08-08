a,b = map(int, input().strip().split())
result = 0
for i in range(1,a+1):
    if a%i == 0:
        result += 1
        if result ==b:
            print(i)
            break

if result<b:
    print(0)