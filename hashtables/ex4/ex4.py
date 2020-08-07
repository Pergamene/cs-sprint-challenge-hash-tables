def has_negatives(a):
  nums = {}
  matches = []
  for num in a:
    if abs(num) in nums:
      matches.append(abs(num))
    else:
      nums[abs(num)] = 1
  return matches

if __name__ == "__main__":
  print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
