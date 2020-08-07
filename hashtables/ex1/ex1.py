def get_indices_of_item_weights(weights, length, limit):
  items = {}
  for i in range(length):
    diff = limit - weights[i]
    if diff in items:
      return (max(i, items[diff]), min(i, items[diff]))
    items[weights[i]] = i
  return None
