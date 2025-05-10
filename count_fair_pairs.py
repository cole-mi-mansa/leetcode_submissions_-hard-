#so, this is a program that looks through an array with n elements, then finds pairs of elements whose sum is greater than or equal to the value "lower" but less that or equal to the value "upper"

def fairPair(arr, lower, upper):
  n = len(arr)
  count = 0
  for i in range(n):
    if i >= 0: #no negative index
      for j in range(n):
        if i < j < n: #no index outside the range
          if lower <= arr[i] + arr[j] <= upper: #declaration of a fair pair
            print(f"({i},{j})")
            count += 1
  if count == 1:
    return f"{count} fair pair"
  elif count == 0:
    return "no fair pair"
  else:
    return f"{count} fair pairs" #desired output 

#test cases  
nums = [0, 1, 7, 4, 4, 5]
print(fairPair(nums, 3, 6)) #should return 6 fair pairs (0,3)(0,4)(0,5)(1,3)(1,4)(1,5)

nums = [1, 7, 9, 2, 5]
print(fairPair(nums, 11, 11)) #should return 1 fair pair (2,3)