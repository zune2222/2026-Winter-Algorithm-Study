import sys
import heapq
input=sys.stdin.readline

a_len=int(input())
a_temp=list(map(int,input().split()))
a_ary=[]
for i in range(a_len):
    a_ary.append((a_temp[i],i))


b_len=int(input())
b_temp=list(map(int,input().split()))
b_ary=[]
for i in range(b_len):
    b_ary.append((b_temp[i],i))


a_ary.sort(reverse=True)
b_ary.sort(reverse=True)

rs=[]

for i in a_ary:
    v,l=i
    if v in b_temp:
        heapq.heappush(rs,(v,l))
        
    





