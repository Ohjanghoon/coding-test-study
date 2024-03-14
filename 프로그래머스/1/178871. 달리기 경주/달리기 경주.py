def solution(players, callings):
    
    rank = {player: i for i, player in enumerate(players)}
    
    for calling_player in callings:
        idx = rank[calling_player]
        rank[calling_player] -= 1
        rank[players[idx - 1]] += 1
        
        # 앞등수와 위치 스왑
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
            
    return players