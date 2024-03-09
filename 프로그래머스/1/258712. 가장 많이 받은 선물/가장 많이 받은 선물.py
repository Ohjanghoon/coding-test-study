def solution(friends, gifts):
    answer = 0
    # 준 선물 내역
    friend_hist_obj = {}
    # 선물 지수
    gift_index = {}
    # 받을 선물 개수
    gift_count = {}
    
    # 나와 친구의 선물 내역
    for me in friends:
        friend_hist_obj[me] = {}
        gift_index[me] = 0
        gift_count[me] = {}
        
        # 나를 제외한 친구 목록
        other_friends = list(filter(lambda x: x != me, friends))
        for friend in other_friends:
            friend_hist_obj[me][friend] = 0
    
    # print("friend_hist_obj ====> ###", friend_hist_obj)
    
    for gift in gifts:
        give, receive = gift.split(' ')
            
        # 주고 받은 수 카운트
        friend_hist_obj[give][receive] += 1
        
        # 선물 지수 계산
        gift_index[give] += 1
        gift_index[receive] -= 1
    
    # print("friend_hist_obj ====> ###", friend_hist_obj)
    # print("gift_index ====> ###", gift_index)
    
    for me in friends:
        for friend, value in friend_hist_obj[me].items():
            me_val = friend_hist_obj[me][friend]
            fr_val = friend_hist_obj[friend][me]
            # 선물을 주고 받은 경우
            if me_val > fr_val:
                gift_count[me][friend] = 1
            elif me_val < fr_val:
                gift_count[friend][me] = 1
            else:
                if gift_index[me] > gift_index[friend]:
                    gift_count[me][friend] = 1
                elif gift_index[me] < gift_index[friend]:
                    gift_count[friend][me] = 1
            
        
        
    # print("friend_hist_obj ===> ", friend_hist_obj)
    # print("gift_index ===> ", gift_index)
    # print("gift_count ===> ", gift_count)
    total_gift_count = []
    for me in friends:
        total_gift_count.append(len(gift_count[me].keys()))
    
    answer = max(total_gift_count)
    return answer