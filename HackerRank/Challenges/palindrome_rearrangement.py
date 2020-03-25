def palindromeRearranging(inputString):
    values = {}
    odd_count = 0
    for i in inputString:
        if i in values:
            values[i] = values[i] + 1
        else:
            values[i] = 1
    for _, v in values.items():
        if v % 2 > 0:
            odd_count += 1

    return odd_count <= 1


print(palindromeRearranging("aabb"))
print(palindromeRearranging("aaadccbb"))
