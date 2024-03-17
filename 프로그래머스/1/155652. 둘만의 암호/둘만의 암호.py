    # 1. 알파벳 리스트 만들기(ASCII 코드 활용, A = 65, a = 97)
    # alphabets = [chr(i) for i in range(97, 97 + 26)]
    
    # 2. 알파벳 리스트 만들기
    # alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]

def solution(s, skip, index):
    answer = ''
    
    # skip 알파벳 제외하고 리스트 만들기
    alphabets = [chr(i) for i in range(97, 97 + 26) if chr(i) not in skip]
    
    for alpha in s:
        alpha_idx = alphabets.index(alpha)
        # 마지막 index를 넘어갈 경우를 대비하여 전체길이로 나눈 나머지 활용
        answer += alphabets[(alpha_idx + index) % len(alphabets)]
    
    # 1차 시도
#     # 알파벳 리스트 만들기(ASCII 코드 활용, A = 65, a = 97)
#     alphabets = [chr(i) for i in range(97, 97 + 26)]
#     print(alphabets)
    
#     # (추가) 알파벳 리스트 만들기
#     # alphabets = [chr(i) for i in range(ord('a'), ord('z') + 1)]
    
#     for alphabet in s:
#         # 현재 알파벳의 인덱스 순번 찾기
#         alpha_idx = alphabets.index(alphabet) % 26
#         skip_idx = 0
        
#         print("alpha_idx ===> ", alpha_idx, "alpha_idx + index + 1 ===> ", alpha_idx + index + 1)
        
#         for i in range(alpha_idx + 1, alpha_idx + index):
#             # 스킵할 알파벳이 포함될 경우
#             if alphabets[i % len(alphabets)] in skip:
#                 print(alphabets[i % len(alphabets)])
#                 skip_idx += 1
        
#         print()
#         print(alpha_idx + skip_idx + index)
#         ch_alphabet = alphabets[(alpha_idx + skip_idx + index) % len(alphabets)]
#         answer += ch_alphabet
    
    return answer