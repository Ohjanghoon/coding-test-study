# numbers: 순서대로 누를 번호 배열
# hand: 왼손/오른손 잡이

def solution(numbers, hand):
    answer = ''
    hand = 'R' if hand == 'right' else 'L'
    hand_dict = {'L': '*', 'R': '#'}
    key = {
        1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*': [3, 0], 0: [3, 1], '#': [3, 2]
    }
    
    for n in numbers:
        # 1, 4, 7 일 경우, 왼손가락 사용
        if n in [1, 4, 7]:
            answer += 'L'
            hand_dict['L'] = n
        # 3, 6, 9 일 경우, 오른손가락 사용
        elif n in [3, 6, 9]:
            answer += 'R'
            hand_dict['R'] = n
        else:
            lk = hand_dict['L']
            rk = hand_dict['R']
            # print(key[lk], key[rk], key[n])
            
            # 현재 왼손, 오른손 위치에서 목적지까지의 거리 계산
            l_dis = abs(key[n][0] - key[lk][0]) + abs(key[n][1] - key[lk][1])
            r_dis = abs(key[n][0] - key[rk][0]) + abs(key[n][1] - key[rk][1])
            
            if l_dis < r_dis:
                answer += 'L'
                hand_dict['L'] = n
            elif l_dis > r_dis:
                answer += 'R'
                hand_dict['R'] = n
            else:
                answer += hand
                hand_dict[hand] = n
            
    
    return answer