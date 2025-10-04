def solution(phone_number):
    answer = []
    real_answer = ''
    P_list = list(phone_number)
    no_star = P_list[-4:]
    P_list.pop(-4)
    P_list.pop(-3)
    P_list.pop(-2)
    P_list.pop(-1)
    for ch in P_list:
        ch = '*'
        answer.append(ch)
    for ch in no_star:
        answer.append(ch)
    return ''.join(answer)