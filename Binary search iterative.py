def binary_search(sorted_list, target):
  left_pointer = 0
  right_pointer = len(sorted_list)
  while left_pointer < right_pointer: 
    mid_idx = (left_pointer + right_pointer)// 2
    mid_val = sorted_list[mid_idx]
    if mid_val == target:
      return mid_idx
    if target < mid_val: 
      right_pointer = mid_idx
    if target > mid_val: 
      left_pointer = mid_idx + 1
  return "Value not in list"
