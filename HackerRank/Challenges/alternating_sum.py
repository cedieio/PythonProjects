def alternatingSums(a):
    arr_sum = [0, 0]
    for i in range(len(a)):
        if (i + 1) % 2 == 1:
            print(1, a[i])
            arr_sum[0] += arr_sum[0] + a[i]
        else:
            print(2, a[i])
            arr_sum[1] += arr_sum[1] + a[i]

    return arr_sum


print(alternatingSums([50, 60, 60, 45, 70]))
