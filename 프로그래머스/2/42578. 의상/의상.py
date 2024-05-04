# clothes: [의상의 이름, 의상의 종류]로 이루어진 행 배열

def solution(clothes):
    answer = 1
    clothes_dict = {}
    
    for c in clothes:
        name, kind = c
        if kind not in clothes_dict.keys():
            clothes_dict[kind] = [name]
        else:
            clothes_dict[kind].append(name)    
    
    for val in clothes_dict.values():
        answer *= len(val) + 1
    
        
    return answer - 1