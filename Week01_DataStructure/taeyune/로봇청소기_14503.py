import sys
input = sys.stdin.readline

# 입력 받기
R, C = map(int, input().split())
cur_r, cur_c, d = map(int, input().split())
area = []
for _ in range(R):
    area.append(list(map(int, input().split())))

# 기본 디렉션 (북, 동, 남, 서)
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
cleaned_area = [[False] * C for _ in range(R)]
result = 0

# 메인 로직
while True :
    if not cleaned_area[cur_r][cur_c] :
        cleaned_area[cur_r][cur_c] = True
        result += 1

    found = False
    for _ in range(4) :
        d = (d + 3) % 4 # 반시계 방향으로 90도 회전한 방향
        next_r, next_c = cur_r + dr[d], cur_c + dc[d]
        if area[next_r][next_c] == 0 and not cleaned_area[next_r][next_c]:
            cur_r, cur_c = next_r, next_c
            found = True
            break

    if not found :
        next_d = (d + 2) % 4 # 바라보는 방향의 뒤쪽 방향
        next_r, next_c = cur_r + dr[next_d], cur_c + dc[next_d]
        if area[next_r][next_c] == 0 :
            cur_r, cur_c = next_r, next_c
        else :
            break

print(result)