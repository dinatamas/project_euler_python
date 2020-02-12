from math import floor, sqrt

def first_non_wheel_prime(wheel):
  """
    Solution via prime checking w/o step.
  """
  i = max(wheel) + 1
  while True:
    for w in wheel:
      if i % w == 0:
        i += 1
        break
      elif w == wheel[-1]:
        return i

def is_prime(n):
  if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    return False
  for i in range(11, floor(sqrt(n))+1, 12):
    print(i, i + 2)
    if n % i == 0 or n % (i+2) == 0:
      return False
  return True

wheel = [2, 3]
next_prime = first_non_wheel_prime(wheel)
original_remainders = []
for w in wheel:
  original_remainders.append(next_prime % w)
remainders = []
i = next_prime + 1
print(f'{next_prime}\t=> ' + ' '.join([str(r) for r in original_remainders]))
while remainders != original_remainders:
  remainders = []
  for w in wheel:
    remainders.append(i % w)
  if 0 not in remainders:
    print(f'{i}\t=> ' + ' '.join([str(r) for r in remainders]))
  i += 1
