def solution(num_list, window_size):
  result = []
  for i in range(len(num_list) - window_size + 1):
      total = 0;
      for j in range(i, i+ window_size):
          total += num_list[j]
      result.append(total / window_size)
          
  
  return result

num_list, window_size = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41], 5
print(solution(num_list, window_size))
