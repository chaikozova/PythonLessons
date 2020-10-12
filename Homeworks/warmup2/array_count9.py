def array_count9(nums):
    count9 = 0
    for i in range(len(nums)):
        if nums[i] == 9:
            count9 += 1
    print(count9)


array_count9([1, 2, 9])
array_count9([1, 9, 9])
array_count9([1, 9, 9, 3, 9])