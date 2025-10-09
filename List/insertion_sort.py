def insertion_sort(nums):
    for i in range(1,len(nums)):
        for j in range(i):
            if nums[j]>nums[i]:
                value = nums.pop(i)
                nums.insert(j,value)
                break
    return nums
