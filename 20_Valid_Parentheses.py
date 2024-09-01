def isValid(s):
    stack = []
    matching_pairs = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if  char in matching_pairs.values():
            print(char)
            stack.append(char)
            
        elif char in matching_pairs.keys():
            if stack and stack[-1] == matching_pairs[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0
        
print(isValid("{([]})"))