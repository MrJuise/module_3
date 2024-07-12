data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def calculate_structure_sum(a):
  if isinstance(a, (int)):
    return a
  if isinstance(a, (str)):
    return len(a)
  if isinstance(a, (list, tuple)):
    if len(a) == 0:
      return 0
    return calculate_structure_sum(a[0]) + calculate_structure_sum(a[1:])
  if isinstance(a, set):
    return calculate_structure_sum(list(a))
  if isinstance(a, dict):
    return calculate_structure_sum(list(a.items()))

result = calculate_structure_sum(data_structure)
print(result)