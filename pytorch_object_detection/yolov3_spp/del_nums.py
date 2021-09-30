



input_nums = '8868863633383886363'

def delet(strings):
    while strings.find('863') != -1:
        strings = strings.replace('863','')    
    print(strings)

# delet(input_nums)


    
input_list = [5,3,1,2,4,5]

def duplicate(nums):
    if not nums or len(nums)<0:
        return False
    for num in nums:
        if num < 0 or num > len(nums) - 1:
            return False
    
    for i in range(len(nums)):
        while nums[i] != i:
            if nums[i] == nums[nums[i]]:
                return nums[i]
            else:
                idx = nums[i]
                nums[i], nums[idx] = nums[idx], nums[i]
    return False
print(duplicate(input_list))
