def solution(s):
    n = len(s)
    answer = 0
    for i in range(n):
        rotated = s[i:] + s[:i] 
        if is_valid(rotated):
            answer += 1
    return answer

def is_valid(seq):
    pairs = {')': '(', '}': '{', ']': '['}
    stack = []
    for ch in seq:
        if ch in '([{':          
            stack.append(ch)
        else:                  
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack            
