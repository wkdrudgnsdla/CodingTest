def solution(clothes):
    cloth_dict = {}

    for name, kind in clothes:
        if kind not in cloth_dict:
            cloth_dict[kind] = 0
        cloth_dict[kind] += 1

    answer = 1

    for count in cloth_dict.values():
        answer *= count + 1
    return answer - 1