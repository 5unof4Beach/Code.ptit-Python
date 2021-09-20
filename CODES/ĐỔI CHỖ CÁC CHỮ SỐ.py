t = int(input())
while t:
    t-=1
    temp = input()
    n=[]
    for i in temp:
        n.append(i)
    if(len(n) == 1):
        print(-1)
        continue
    i = len(n) - 2
    while i>=0 and n[i]<=n[i+1]:
        i-=1
    if i < 0:
        print(-1)
    else:
        max_idx = i+1
        for j in range(i+1,len(n)):
            if n[j] < n[i] and n[j]>n[max_idx]:
                max_idx = j
        n[i],n[max_idx] = n[max_idx],n[i]
        if n[0] == '0':
            print(-1)
        else:
            for i in n:
                print(i,end="")
            print()

