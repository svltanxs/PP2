
def spy_game(nums):
    for i in nums:
        if(nums[i] == 0 and nums[i + 1] == 0 and nums[i + 2] == 7):
            print("True")
spy_game([1,2,4,0,0,7,5]) 
spy_game([1,0,2,4,0,5,7]) 
spy_game([1,7,2,0,4,5,0]) 