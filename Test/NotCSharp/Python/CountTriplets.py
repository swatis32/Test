# http://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/
import itertools
alist = list()

def countTriplets(a, summ):
    count = 0
    for subset in itertools.combinations(a,3):
        if sum(subset) < summ:
            count = count + 1
            alist.append(subset)
    return count

print(countTriplets([1, 2, 3, 4, 5], 10))
print(alist)
alist.clear()


def countTriplets2(a, summ):
    a = sorted(a)
    count = 0
    lena = len(a)
    for i in range(0, lena - 2):
        j = i + 1
        k = len(a) - 1
        while j < k:
            if a[i] + a[j] + a[k] < summ:
                alist.append([a[i], a[j], a[k]])
                k = k - 1
            else:
                count = count + k - j
                j = j + 1

    return count

print(countTriplets2([1, 2, 3, 4, 5], 10))
print(alist)