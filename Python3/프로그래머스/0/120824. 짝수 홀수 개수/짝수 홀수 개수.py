def solution(num_list):
    answer = []
    jjack = 0
    hole = 0
    for i in num_list:
        if i % 2 == 0:
            jjack += 1
        else:
            hole += 1
    answer.insert(0, jjack)
    answer.insert(1, hole)
    return answer