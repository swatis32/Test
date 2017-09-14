# https://www.hackerrank.com/challenges/ctci-balanced-brackets/problem
dict_exp = dict()
dict_exp['{'] = '}'
dict_exp['['] = ']'
dict_exp['('] = ')'
'''
def is_matched2(expression):
    lenexp = len(expression)
    j = lenexp - 1
    if lenexp % 2 == 1:
        return False
    for i in range(0, int(lenexp/2)):
        if expression[i] not in dict_exp.keys():
            return False
        exp_i = dict_exp[expression[i]]
        if exp_i != expression[j]:
            return False
        j -= 1
    return True
'''

# Correct method is to take a stack - if you find {,[,( then push },],) - if you find },],), pop last element from
# stack and check if it is equal to },],) - if not, then not in sequence. Return whether length of stack is 0
def is_matched(expression):
    if expression is None:
        return True
    if expression is '':
        return True
    if len(expression) % 2 == 1.0:
        return False
    first = list(expression[0: int(len(expression) / 2)])
    second = list(reversed(expression[int(len(expression) / 2):]))
    for i in range(0, len(first)):
        if dict_exp[first[i]] != second[i]:
            return False
    return True

print(is_matched('{{[[(())]]}}'))

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

# inputs: https://hr-testcases-us-east-1.s3.amazonaws.com/23954/input09.txt?AWSAccessKeyId=AKIAJ4WZFDFQTZRGO3QA&Expires=1505285938&Signature=lDSWfst%2BNiH8Ff0x7NQ9KOWad7A%3D&response-content-type=text%2Fplain