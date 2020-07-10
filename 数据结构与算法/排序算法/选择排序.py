def selectionSort(nums):
    for i in range(len(nums) - 1):  # 遍历len(nums)-1次
        minIndex = i
        for j in range(i + 1, len(nums)):   # 更新最小值索引
            if nums[j] < nums[minIndex]:
                minIndex = j
        nums[i], nums[minIndex] = nums[minIndex], nums[i]   # 把最小数交换到前
    return nums