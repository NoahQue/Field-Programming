# input:
# num: a list of Integer or Decimal
# symbol: a list of (+, - , *, /)

# output:
# ans: the result of the calculation

def computeAns(num, symbol):

    temp_num = []
    temp_symbol = []
    symbol = symbol[::-1]
    num = num[::-1]

    while len(symbol):
        temp = symbol.pop()
        if temp == '+' or temp == '-':
            temp_symbol.append(temp)
            temp_num.append(num.pop())
            print(temp_num, temp_symbol)

        elif temp == '*' or temp == '/':
            f1 = num.pop()
            f2 = num.pop()
            if temp == '*':
                ans = f1 * f2
            else:
                ans = f1 / f2
            num.append(ans)

    if len(num) != 0:
        temp_num.append(num.pop())

    print(temp_num, temp_symbol)
    ans = temp_num[0]
    for i in range(len(temp_symbol)):
        if temp_symbol[i] == '+':
            ans += temp_num[i + 1]
        elif temp_symbol[i] == '-':
            ans -= temp_num[i + 1]

    return ans


def computeAns2(num, symbol):
    if symbol[0] == '+':
        ans = num[0] + num[1]
    elif symbol[0] == '-':
        ans = num[0] - num[1]
    elif symbol[0] == '*':
        ans = num[0] * num[1]
    else:
        ans = num[0] / num[1]
    return ans


num1 = [100, 200, 300, 400]
num2 = [2.2, 200, 123, 300]
num3 = [5, 2, 3, 1]

symbol1 = ['+', '-', '*']
symbol2 = ['-', '-', '-']
symbol3 = ['/', '/', '/']

ans1 = num1[0] + num1[1] - num1[2] * num1[3]
temp_ans1 = computeAns(num1, symbol1)
print(temp_ans1, ans1)
print(temp_ans1 == ans1)

ans2 = num2[0] - num2[1] - num2[2] - num2[3]
temp_ans2 = computeAns(num2, symbol2)
print(temp_ans2, ans2)
print(temp_ans2 == ans2)

ans3 = num3[0] / num3[1] / num3[2] / num3[3]
temp_ans3 = computeAns(num3, symbol3)
print(temp_ans3, ans3)
print(temp_ans3 == ans3)
