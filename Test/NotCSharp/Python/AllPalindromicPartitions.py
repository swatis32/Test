# http://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/
def allPalindromicPartitions(a):
    lena = len(a)
    partitions = list()
    list1 = list(a)
    partitions.extend(list1)
    for i in range(2, lena + 1):
        for j in range(0, lena - i + 1):
            b = a[j:j+i]
            if checkIfStringIsPalindrome(b):
                partitions.append(b)

    return partitions


def checkIfStringIsPalindrome(b):
    lenb = int(len(b)/2)
    if len(b) % 2 == 0:
        first = b[:lenb]
        second = b[lenb:]
    else:
        first = b[0: lenb]
        second = b[lenb + 1:]

    if second[::-1] == first:
        return True
    else:
        return False



allPalindromicPartitions('nitin')

