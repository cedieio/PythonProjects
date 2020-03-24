def addBorder(picture):
    arr_with_border = []
    arr_with_border.append("*" * (len(picture[0]) + 2))
    for i in picture:
        arr_with_border.append("*" + i + "*")
    arr_with_border.append("*" * (len(picture[0]) + 2))
    print(arr_with_border)


addBorder(["abc", "ded"])
