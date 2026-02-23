import sys
input=sys.stdin.readline

N,C = map(int,input().split())
houses=[int(input()) for _ in range(N)]

houses.sort()

start=1
end=houses[-1]-houses[0]
result=0

while start<=end:
    mid=(start+end)//2

    count=1
    current_last_install=houses[0]

    for i in range(1,N):
        if houses[i]-current_last_install >= mid:
            count+=1
            current_last_install=houses[i]

    if count>=C:
        result=mid
        start=mid+1

    else:
        end=mid-1
print(result)
