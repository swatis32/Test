# https://www.youtube.com/watch?v=lDYIvtBVmgo
from copy import deepcopy


def palindrome_partition(arr):
    lenarr = len(arr)
    pp = [[1000] * lenarr for x in range(lenarr)]
    for i in range(lenarr):
        pp[i][i] = 0

    length = 1
    while length <= lenarr:
        i = 0
        j = length
        while j < lenarr:
            x = deepcopy(arr[i:j+1])
            if list(x) == list(reversed(list(x))):
                pp[i][j] = 0
            else:
                pp[i][j] = 1 + min(pp[i+1][j], pp[i][j-1])
            i += 1
            j += 1
        length += 1

    return pp[0][lenarr - 1]


print(palindrome_partition('abcbm'))
print(palindrome_partition('aaaaa'))
print(palindrome_partition('nitin'))
print(palindrome_partition('shasha'))
print(palindrome_partition('madame'))