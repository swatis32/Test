# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem
n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

total_swap = 0
for i in range(0,len(a)):
    swap = 0
    for j in range(0, len(a) - 1):
        if a[j] > a[j+1]:
            temp = a[j]
            a[j] = a[j+1]
            a[j+1] = temp
            swap +=1
    if (swap == 0):
        break
    total_swap += swap

print("Array is sorted in", total_swap, "swaps.")
print("First Element:", a[0])
print("Last Element:", a[len(a) - 1])