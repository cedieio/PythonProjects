def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    arm_values = []
    arm_values.append(str(yourLeft) + "_left")
    arm_values.append(str(friendsLeft) + "_left")
    arm_values.append(str(yourRight) + "right")
    arm_values.append(str(friendsRight) + "right")
    return True


print(areEquallyStrong(10, 15, 15, 9))
