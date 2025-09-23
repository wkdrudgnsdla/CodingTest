def solution(my_string, overwrite_string, s):
    return my_string[0:s:1]+overwrite_string[::1]+my_string[s+len(overwrite_string)::1]
