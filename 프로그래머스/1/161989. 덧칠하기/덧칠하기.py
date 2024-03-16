# n: 벽 길이(m)
# m: 롤러 길이(m)

def solution(n, m, section):
    
    paint_wall = 0
    count = 0
    
    # 2차 시도
    for again_paint in section:
        # 칠한 벽보다 칠할 벽의 번호가 클 경우
        if again_paint > paint_wall:
            paint_wall = again_paint + m - 1
            count += 1
    
    # 1차 시도
#     # 현재 벽 리스트(-1: 다시 칠할 벽, 0: 칠해진 벽)
#     curr_wall = []
#     for i in range(1, n + 1):
#         if i in section:
#             curr_wall.append(-1)
#         else:
#             curr_wall.append(0)
            
#     # 벽 칠하는 횟수
#     count = 0
#     for i in curr_wall:
#         if i == 0:
#             continue
        
#         count += 1
        
#         # 다시 칠할 벽 위치 찾기
#         idx = curr_wall.index(-1)
        
#         # 다시 칠할 벽 기준으로 롤러의 길이 만큼 페인트를 칠함
#         for i in range(idx + m):
#             # 롤러가 벽 길이를 넘어서 칠할 경우 멈춤
#             if i >= n:
#                 break
#             if curr_wall[i] == 0:
#                 continue
            
#             curr_wall[i] = 0
        
#         # 벽이 다 칠해졌을 경우 종료
#         if -1 not in curr_wall:
#             break
    
    return count