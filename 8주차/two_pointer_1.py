def sum_function(nums, target):
    #양쪽 끝점에서 각 포인터 시작
    left, right = 0, len(nums)-1

    while not left == right:   # 포인터들이 겹치면 끝
       if nums[left] + nums[right] > target:
           right -= 1
       elif nums[left] + nums[right] < target:
           left += 1
       elif nums[left] + nums[right] == target:
           return nums[left], nums[right], left, right

    return 0, 0, 0, 0
    
# Input arr and target    
arr = [2, 7, 11, 15]
target = 26

left_num, right_num, left_idx, right_idx = sum_function(arr, target)
if left_idx == right_idx:
    print(f"더해서 target({target})이 되는 두 원소가 없습니다.")
else:
    print(f"더해서 target({target})이 되는 두 원소 : {left_num} (index = {left_idx}), {right_num} (index = {right_idx})")
