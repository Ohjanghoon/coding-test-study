def solution(nums):
    selected_mon = []
    select_count = len(nums) // 2
    
    for i in nums:
        if i not in selected_mon and len(selected_mon) < select_count:
            selected_mon.append(i)
            
    answer = len(selected_mon)
    return answer