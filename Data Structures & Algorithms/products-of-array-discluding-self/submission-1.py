class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        postfix = [1]*len(nums)
        output = [1]*len(nums)

        for idx in range(len(nums)):
            if idx == 0:
                prefix[idx] = nums[idx]
            else:
                prefix[idx] = prefix[idx-1]*nums[idx]

        for idx in range((len(nums)-1), -1, -1):
            if idx == len(nums)-1:
                postfix[idx] = nums[idx]
            else:
                postfix[idx] = nums[idx]*postfix[idx+1]

        for idx in range(len(output)):
            if idx == 0:
                output[idx] = postfix[idx+1]
            elif idx == len(output) - 1:
                output[idx] = prefix[idx-1]
            else:
                output[idx] = prefix[idx-1]*postfix[idx+1]

        return output




