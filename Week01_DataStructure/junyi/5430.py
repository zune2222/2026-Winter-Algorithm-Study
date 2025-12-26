t=int(input())
for _ in range(t):
    stat=False
    p=input()
    n=int(input())
    ary=input()
    if not n==0:
        ary=list(map(int,ary[1:-1].split(",")))
    else:
        ary=list()
    skip=False
    for s in p:
        skip=False
        if s=='R':
            stat=not stat
        if s=='D':
            if len(ary)==0:
                print("error")
                skip=True
                break
            if stat:
                ary.pop()
            else:
                ary.pop(0)
    if stat:
        ary.reverse()
    if not skip:
        print("["+",".join(map(str,ary))+"]")
