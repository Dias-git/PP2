def has_33(nums):
    for i in range(len(nums) - 1):  #index==len  bolu ushin
        if nums[i] == nums[i+1] == 3:
            return True
    return False

# Проверка
print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False