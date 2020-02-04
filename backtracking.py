# lexicographical permutation iterator
def next_permutation(array):
    i = len(array) - 1
    while i > 0 and array[i-1] > array[i]:
        i -= 1
    if i == 0:
        return array
    print(i)
    res = array.copy()
    j = i
    # you can improve the following code using sorted() and tuple assignment
    # and even the fact that you can append/remove stuff from lists
    while j < len(res):
        print(res)
        res[j-1] = array[j]
        j += 1
    res[len(res)-1] = array[i-1]
    return res

# backtracking

# memoization

# dynamic programming