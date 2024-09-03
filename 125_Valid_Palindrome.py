def isPalindrome(s):
    word = "".join(char.lower() for char in s if char.isalnum())
    reversed_word = word[::-1]
    return word == reversed_word

print(isPalindrome("Mamam"))
# print(isPalindrome("A man, a plan, a canal: Panama"))