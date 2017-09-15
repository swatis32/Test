# http://www.geeksforgeeks.org/primality-test-set-1-introduction-and-school-method/
import math

p = int(input().strip())
for a0 in range(p):
    n = int(input().strip())
    isPrime = True
    if n == 2 or n == 1:
        print('Prime')
        continue
    if n % 2 == 0 or n % 3 == 0:
        print('Not prime')
        continue
    k = 1

    # 6k + 1 or 6k - 1
    six_k_plus_1 = 6 * k + 1
    six_k_minus_1 = 6 * k - 1
    is_prime = False
    while six_k_minus_1 <= n:
        if six_k_plus_1 == n or six_k_minus_1 == n:
            print('Prime')
            is_prime = True
            break
        else:
            k = k + 1
            six_k_plus_1 = 6 * k + 1
            six_k_minus_1 = 6 * k - 1

    if (is_prime == False):
        print('Not prime')


'''
static bool isPrime(int n)
{
    // Corner cases
    if (n <= 1)  return false;
    if (n <= 3)  return true;
 
    
    if (n%2 == 0 || n%3 == 0) return false;
 
    // why this? any prime number is of the form 6k +/- 1, why?
    // Number cannot be 6k + 2 => div by 2, cant be 6k+3 or 6k+4, the only one left is 6k+5, which is essentially 6k-1
    for (int i=5; i*i<=n; i=i+6)
        if (n%i == 0 || n%(i+2) == 0)
           return false;
 
    return true;
    
}

'''