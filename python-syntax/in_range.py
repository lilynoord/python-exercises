def in_range(nums, lowest, highest):
    for each in nums:
        if each >= lowest and each <= highest:
            print(each,"fits")

print("IN_RANGE")
in_range([10, 20, 30, 40, 50], 15, 30)            
