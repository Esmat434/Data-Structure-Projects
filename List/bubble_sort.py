def bubble_sort(nums):
    for i in nums:
        flag = False
        for j in range(len(nums)-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                flag=True
        if not flag:
            return nums
    return nums