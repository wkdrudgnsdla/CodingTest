def solution(babbling):
    answer = 0
    for word in babbling:
        joka_say = {"aya", "ye", "woo", "ma"}
        while True:
            if word[:3] in joka_say:
                joka_say.discard(word[:3])
                word = word[3:]
            elif word[:2] in joka_say:
                joka_say.discard(word[:2])
                word = word[2:]
            else: break
        if word == "":
            answer += 1
    return answer