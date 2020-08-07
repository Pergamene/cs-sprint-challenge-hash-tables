def intersection(arrays):
  intersection = dict.fromkeys(arrays[0], 1)
  for i in range(1, len(arrays)):
    new_intersection = {}
    for num in arrays[i]:
      if num in intersection:
        new_intersection[num] = 1
    intersection = new_intersection
  return list(intersection.keys())

if __name__ == "__main__":
  arrays = []
  arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
  arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
  arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])
  print(intersection(arrays))
