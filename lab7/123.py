def pow_l(num, degree):
    result = 1
    while degree != 0:
        if degree % 2 != 0:
            result *= num
            result %= 2022
            degree -= 1
        else:
            num *= num
            num %= 2022
            degree /= 2
    return result

n = int(input())
q = n // 5
p = n // 2
first_p = ((n - (q * 5)) // 2)
first = pow_l(2,first_p) * pow_l(5,q)
second_q = ((n - (p * 2)) // 5)
second = pow_l(2,p) * pow_l(5,second_q)
print(max(first, second))