class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()

        for i in range(len(nums)-2):
            
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i]>0:
                break

            l = i+1
            r = len(nums)-1

            while l < r:
                target = nums[l] + nums[r] + nums[i]
                if target > 0:
                    r -= 1
                elif target < 0:
                    l += 1
                else:
                    value = [nums[i], nums[l], nums[r]]
                    output.append(value)
                    l+=1
                    r-=1
                    while l < r and nums[l] == nums[l-1]:
                        l+=1
                    while l < r and nums[r] == nums[r+1]:
                        r-=1

                    
        return output
        