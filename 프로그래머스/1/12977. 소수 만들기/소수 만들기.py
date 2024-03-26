def solution(nums):
    answer = 0
    
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                addition = nums[i] + nums[j] + nums[k]
                
                is_prime = False
                for x in range(2, addition):
                    if addition % x == 0:
                        is_prime = False
                        break
                    else:
                        is_prime = True
                        
                if is_prime: answer += 1
        
    return answer