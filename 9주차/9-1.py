def palindrom_bf(word):
    for i in range(0, len(word)):
        if isPalindrome(word[i:]):
            return word + reverse(word[:i]), len(word + reverse(word[:i]))
    return word + reverse(word), len(word + reverse(word))

def isPalindrome(word):
    if len(word)%2==0:
        return word[:len(word)//2]==reverse(word[len(word)//2:])
    else:
        return word[:len(word)//2]==reverse(word[len(word)//2+1:])
    
def reverse(word):
    return "".join(reversed(word))

word = str(input("문자열을 입력해주세요 : "))
print(palindrom_bf(word))
