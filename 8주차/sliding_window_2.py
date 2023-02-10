def solution(s):
    ans = 0   # 부분 문자열의 길이
    left_cursor = 0   # 왼쪽 포인터
    used = {}   # window로 검사한 문자 인덱스 정보 저장

    for right_cursor, char in enumerate(s):
       if (char in used) and (left_cursor <= used[char]):
            left_cursor = used[char] + 1
       else:
            if right_cursor - left_cursor > ans:
                ans = right_cursor - left_cursor
            used[char] = right_cursor
    return ans

str = 'pwwkew'
print(f"{str}의 가장 긴 부분 문자열의 길이 : {solution(str)}")
