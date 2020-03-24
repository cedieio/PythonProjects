def arrayChange(inputArray):
    totalSum = 0
    for i in range(len(inputArray) - 1):
        if inputArray[i] >= inputArray[i + 1]:
            missingVal = (inputArray[i] - inputArray[i + 1]) + 1
            inputArray[i + 1] += missingVal
            totalSum += missingVal
    print(inputArray)
    return totalSum


print(arrayChange([1, 1, 1, 1]))
