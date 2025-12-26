n=int(input())
ary=list(map(int,input().split()))
stk=[]
rst=[]
for i in range(n):
    current_height=ary[i]
    current_index=i+1

    while stk and stk[-1][0] < current_height:
        stk.pop()
    if stk:
        rst.append(stk[-1][1])
    else:
        rst.append(0)
    stk.append([current_height,current_index])

print(*rst)