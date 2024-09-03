def lengthOfLastWord(s):
    word = s.split()
    if not word:
        return 0
    return len(word[-1])
    
    
print(lengthOfLastWord("My Name is Abdullah"))