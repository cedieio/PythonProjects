def areSimilar(a, b):
    failures = []
    for i in range(len(a)):
        if a[i] != b[i]:
            failures.append(i)

    if len(failures) == 2:
        a[failures[0]], a[failures[1]] = a[failures[1]], a[failures[0]]
        return a == b
    elif len(failures) != 0:
        return False
    else:
     return True


areSimilar([1, 2, 3], [2, 1, 3])
