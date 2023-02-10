def solution(height):
    if not height:
        return 0

    vol = 0   # 누적된 물의 양
    left, right = 0, len(height) - 1   # Two Pointer 정의
    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
        
        if left_max <= right_max:
            vol += left_max - height[left]
            left += 1
        else:
            vol += right_max - height[right]
            right -= 1
    
    return vol

height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f"{height}에 쌓인 물의 양 : {solution(height)}")
