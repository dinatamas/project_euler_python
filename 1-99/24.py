digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def next_cyclic_ind(array, ind):
  return (ind + 1) % (len(array))

def next_permutation(permutation):
  i = 0
  while i < len(permutation)-1 and permutation[i] < permutation[i+1]:
    i += 1
  if i == len(permutation)-1:
    permutation[-1], permutation[-2] = permutation[-2], permutation[-1]
  else:
    if permutation[i:] == sorted(permutation[i:], reverse=True):
      j = i
      while j < len(permutation)-1 and permutation[j] != permutation[i-1]+1:
        j += 1
      permutation[j], permutation[i-1] = permutation[i-1], permutation[j]
      permutation[i:] = sorted(permutation[i:])
    else:
      while permutation[i] > permutation[i+1]:
        i += 1
      permutation[i:] = sorted(permutation[i:], reverse=True)

permutation = digits
print(permutation)
for i in range(0, 10):
  next_permutation(permutation)
  print(permutation)

"""
permutation = digits
for i in range(2, 1000001):
  permutation = next_permutation(array, permutation)

print(permutation)
"""