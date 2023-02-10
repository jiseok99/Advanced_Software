from collections import Counter

def findAnagrams(s, p):
    cnt = Counter(p)
    ans = []
    l = 0

    """ Input your code here """
    part = Counter(s[:len(p)-1])

    for l in range(len(p)-1, len(s)):
        start = l - (len(p) - 1)

        part[s[l]] += 1

        if part == cnt:
            ans.append(start)
            
        part[s[start]] -= 1

        if part[s[start]] == 0:
            del part[s[start]]
    
    return ans
  
s1, s2 = "cbaebabacd", "abc"
print(f"애너그램 시작 인덱스 : {findAnagrams(s1, s2)}")
