def solution(str1, str2):
    print('"', end="")
    st = ""
    for i in range(len(str1)):
        print(str1[i] + str2[i],end="")
        st += str1[i] + str2[i]
    print('"', end="")
    return st