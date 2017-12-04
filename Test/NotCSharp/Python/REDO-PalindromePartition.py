# https://www.youtube.com/watch?v=lDYIvtBVmgo
from copy import deepcopy

# This solution is not optimal, optimal is O(n2)
# https://www.youtube.com/watch?v=WPr1jDh3bUQ
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
                k = i
                mini = 1000
                # THIS IS SUPER IMPORTANT
                # WE ARE SPLITTING AT EACH POINT BETWEEN ARR[i:j] and getting the min
                while k < j:
                    temp = 1 + pp[i][k] + pp[k+1][j]
                    if temp < mini:
                        mini = temp
                    k += 1
                pp[i][j] = mini
            i += 1
            j += 1
        length += 1

    palindromes = set()
    for i in range(lenarr):
        for j in range(lenarr):
            if pp[i][j] == 0:
                palindromes.add(arr[i:j+1])

    print("The palindromes for arr:{0} are".format(arr))
    print(palindromes)
    print("The minimum number of partitions required are")
    return pp[0][lenarr - 1]


print(palindrome_partition('abcbm'))
print(palindrome_partition('aaaaa'))
print(palindrome_partition('nitin'))
print(palindrome_partition('shasha'))
print(palindrome_partition('madame'))
print(palindrome_partition('aabcac'))

# O(n2) solution is defined below
def pal_partition(arr):

    pal = [[False] * len(arr) for x in range(len(arr))]
    for i in range(len(arr)):
        pal[i][i] = True

    # cuts is the number of partitions needed until point i
    '''
    b a n a n a
    0 1 2 3 4 5
    
    cuts[1] = number of cuts needed for string arr[0:2] = "ba" = 1
    cuts[1] = 1
    cuts[len(arr)-1] = answer needed
    '''
    cuts = [1000] * len(arr)
    l = 2

    while l <= len(arr):
        i = 0
        j = l
        while j < len(arr):
            if arr[i] == arr[j]:
                if i == j-1:
                    pal[i][j] = True
                else:
                    pal[i][j] = pal[i+1][j-1]
            i += 1
            j += 1
        l += 1

    cuts[0] = 0
    for i in range(1, len(arr)):
        if pal[0][i] is True:
            cuts[i] = 0
        else:
            minicut = i
            # start splitting the string at each point in the string
            for j in range(i):
                # didnt understand this completely
                if pal[j+1][i] is True and minicut > 1 + cuts[j]:
                    minicut = 1 + cuts[j]
            cuts[i] = minicut
    print("Palindrome partition 2 result")
    return cuts[len(arr) - 1]

print(pal_partition('banana'))
print(pal_partition('abcbm'))
print(pal_partition('aaaaa'))
print(pal_partition('nitin'))
print(pal_partition('shasha'))
print(pal_partition('madame'))
print(pal_partition('aabcac'))
