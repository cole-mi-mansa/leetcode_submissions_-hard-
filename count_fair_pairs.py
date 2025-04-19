def fairPair(arr, lower, upper):
  n = len(arr)
  count = 0
  for i in range(n):
    if i >= 0:
      for j in range(n):
        if i < j < n:
          if lower <= arr[i] + arr[j] <= upper:
            print(f"({i},{j})")
            count += 1
  if count == 1:
    return f"{count} fair pair"
  elif count == 0:
    return "no fair pair"
  else:
    return f"{count} fair pairs"
  
nums = [0, 1, 7, 4, 4, 5]
print(fairPair(nums, 3, 6))

nums = [1, 7, 9, 2, 5]
print(fairPair(nums, 11, 11))