# park: 공원 문자열 배열
# routes: 로봇 강아지 수행 문자열 배열
# return: 로봇 강아지 명령 수행 후 놓인 위치 좌표 [세로, 가로]

def solution(park, routes):
    HEIGHT = len(park)
    WIDTH = len(park[0])
    
    # 시작 위치 좌표 찾기
    y, x = 0, 0
    for i, row in enumerate(park):
        if 'S' in row:
            y = i
            x = row.index('S')
            break
    
    # 이동하는 동안 경로를 이탈했는지, 장애물을 만났는지 체크하기 위한 좌표
    tmp_y, tmp_x = y, x
    
    move = {"E": [0, 1], "W": [0, -1], "S": [1, 0], "N": [-1, 0]}
    for route in routes:
        # 방향과 거리
        direction, distance = route.split(" ")
        
        for i in range(int(distance)):
            tmp_y += move[direction][0]
            tmp_x += move[direction][1]
            print("{} ===> ({}, {})".format(route, tmp_y, tmp_x))
            
            # 공원을 벗어날 경우
            if 0 <= tmp_y <= HEIGHT - 1 and 0 <= tmp_x <= WIDTH - 1:
                # 장애물을 지나간 경우
                if park[tmp_y][tmp_x] == "X":
                    tmp_y, tmp_x = y, x
                    break
            else:
                tmp_y, tmp_x = y, x
                break
                    
        y, x = tmp_y, tmp_x
            
        
    
    return [y, x]