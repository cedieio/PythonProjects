def reverseInParentheses(inputString):
    for i in reversed(range(len(inputString))):
        if inputString[i] == "(":
            innerString = inputString[i:]
            for v in range(len(innerString)):
                if innerString[v] == ")":
                    print("###", innerString[1:v][::-1])
                    inputString = inputString.replace(
                        inputString[i : i + v + 1],
                        innerString[1 : v + 1][::-1].replace("(", "").replace(")", ""),
                    )
                    break
    return inputString


print(reverseInParentheses("foo(bar(baz))blim"))

reverseInParentheses("foo(bar(baz))blim")

reverseInParentheses("(bar)")
## foo(bar)baz(blim)
