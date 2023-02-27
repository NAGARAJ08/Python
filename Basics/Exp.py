def power(base_num,pow_num):
    res = 1
    for idx in range(pow_num):
        res = res * base_num
    return res

print(power(5,5))
