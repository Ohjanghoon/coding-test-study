def solution(board, moves):
    answer = 0
    board_dict = {}
    basket = []
    for i in range(len(board)):
        tmp = []
        for j in range(len(board[i])):
            if board[j][i] == 0:
                continue
            tmp.append(board[j][i])
        board_dict[i + 1] = tmp
    # print(board_dict)
    
    for m in moves:
        # print(m, board_dict)
        # 해당 줄이 전부 빈 칸일 경우
        if len(board_dict[m]) == 0:
            continue
        else:
            # 가장 위에 있는 인형을 집음
            basket.append(board_dict[m].pop(0))
        
        # 바구니에 2개 이상 쌓여있고, 마지막에 쌓인 2개가 같은 경우 => 터트림
        if len(basket) > 1 and basket[-1] == basket[-2]:
            del basket[-2]
            del basket[-1]
            answer += 2
        # print("basket ===> {}".format(basket))
        # print("board_dict ===> {}".format(board_dict))
            
    return answer