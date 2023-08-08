while True:
    l = []
    n = int(input())
    if n == -1:
        break
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    l = l[:-1]
    if sum(l)==n:
        print(f"{n} = " + ' + '.join([str(i) for i in l]))
    else:
        print(f"{n} is NOT perfect.")