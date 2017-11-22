# https://codefights.com/interview/At83id5ZCwo2mNzdm
def multiplyTwoStrings(s1, s2):
    s1_int = int(s1)
    s2_int = int(s2)
    return str(s1_int * s2_int)
    pass

multiplyTwoStrings("23", "34")


def multiply(s1, s2):
    m = len(s1)
    n = len(s2)
    res = 0;
    for i in range(m):
        a = int(s1[m - i - 1])
        for j in range(n):
            b = int(s2[n - j - 1])
            res += a * b * (10 ** (i + j))
    return res

print(multiply("23", "34"))


'''
   30    4
20 600   80
3  90    12

23 x 34 = 782
600 + 90 + 80 +12 = 782

'''