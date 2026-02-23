import sys
input = sys.stdin.readline

s = input().strip()
stack = []
temp = 1
ans = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        temp *= 2
    elif s[i] == '[':
        stack.append(s[i])
        temp *= 3
    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            ans = 0
            break
        if s[i-1] == '(':
            ans += temp
        stack.pop()
        temp //= 2
    elif s[i] == ']':
        if not stack or stack[-1] == '(':
            ans = 0
            break
        if s[i-1] == '[':
            ans += temp
        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(ans)