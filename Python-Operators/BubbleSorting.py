numInput = input("Please input your list comma separated : ")

nums = numInput.split(",")
swapped = True
while swapped:
    swapped = False
    for i in range(len(nums) - 1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            swapped = True


print(nums)
