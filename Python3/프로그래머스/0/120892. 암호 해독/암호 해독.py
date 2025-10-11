def solution(cipher, code):
    answer = ''
    chipher_list = list(cipher)
    for i in range(1, len(chipher_list) + 1):
        if i % code == 0:
            answer += chipher_list[i-1]
    return answer