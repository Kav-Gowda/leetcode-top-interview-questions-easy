def rotate(nums, k):
    n = len(nums)
    k %= n
    temp = [0] * n
    
    for i in range(n):
        temp[(i + k) % n] = nums[i]
    
    nums[:] = temp
