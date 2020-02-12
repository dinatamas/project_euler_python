# Solutions include:
#  - Prime sieves, especially segmented prime sieves.
#  - Brute force checks, with a step of 1 or with finding the optimal step after each iteration.

"""
  When given a prime number, find the smallest prime that is bigger than the number provided.
"""

"""
  When given a prime number, find the smallest prime that is bigger than the prime provided.
"""

"""
  When given a prime number, find the biggest prime that is smaller than the number provided.
"""

"""
  When given a prime number, find the biggest prime that is smaller than the prime provided.
"""

"""
  When given a list of consequtive prime numbers starting from 2, find the smallest prime that is not included in the list.
"""

"""
  When given a list of consequtive prime numbers, find the smallest prime that is not included in the list.
"""

###

def first_non_wheel_prime_1(wheel):
  """
    Solution via prime checking w/ step.
  """
  count = 0
  i = max(wheel) + 1
  while True:
    step = 1
    for w in wheel:
      count += 1
      if i % w == 0:
        i += step
        break
      elif i % w < step:
        step = i % w
      elif w == wheel[-1]:
        return (i, count)