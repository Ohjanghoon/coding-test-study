# board: 보드의 각 칸에 칠해진 색깔 이름 이차원 배열
# h, w: 고른 칸의 위치
# return - 이웃한 칸 들 중 같은 색으로 칠해져 있는 칸의 개수

def solution(board, h, w):
    n = len(board)
    count = 0
    adjoin_color = []
    
    selected_color = board[h][w]
    if h + 1 <= n - 1:
        adjoin_color.append(board[h + 1][w])
    if 0 <= h - 1:
        adjoin_color.append(board[h - 1][w])
    if w + 1 <= n - 1:
        adjoin_color.append(board[h][w + 1])
    if 0 <= w - 1:
        adjoin_color.append(board[h][w - 1])
    
    return adjoin_color.count(selected_color)