import sys

input=sys.stdin.readline

N=int(input())

words=[input().strip() for _ in range(N)]

alpha_dict={}

for word in words:
    length=len(word)
    for i in range(length):
        char=word[i]
        power=10**(length-1-i)
        if char in alpha_dict:
            alpha_dict[char]+=power
        else:
            alpha_dict[char]=power

sorted_values=sorted(alpha_dict.values(),reverse=True)

num=9
rs=0
for i in sorted_values:
    rs+=num*i
    num-=1
print(rs)
