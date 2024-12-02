def difference(nums):
    for i in range(0, len(nums)-1):
        if abs(nums[i]-nums[i+1]) < 1 or abs(nums[i]-nums[i+1]) > 3:
            return False
    return True
        
def increase(nums):
    for i in range(0, len(nums)-1):
        if nums[i] > nums[i+1]:
            return False
    return True

def decrease(nums):
    for i in range(0, len(nums)-1):
        if nums[i] < nums[i+1]:
            return False
    return True


counter = 0
with open("input.txt") as file:
    for line in file:
        nums = []
        tempList = line.strip().split(" ")
        for item in tempList:
            nums.append(int(item))
        
        if difference(nums) and (increase(nums) or decrease(nums)):
            counter += 1
    file.close()

print(counter)