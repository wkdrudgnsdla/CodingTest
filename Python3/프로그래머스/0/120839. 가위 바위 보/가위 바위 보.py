def solution(rsp):
    answer = ''
    rsp_list = list(rsp)
    for ch in rsp_list:
        if ch == "2":
            answer += "0"
        elif ch == "0":
            answer += "5"
        elif ch == "5":
            answer += "2"
    return answer