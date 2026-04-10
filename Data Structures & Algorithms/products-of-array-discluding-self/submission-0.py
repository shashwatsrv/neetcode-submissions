class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        otp=[]
        count=-1
        for j in nums:
            mult=[]
            count+=1
            for i in range(len(nums)):
                if(i==count):
                    mult.append(1)
                else:
                    mult.append(nums[i])
            result=math.prod(mult)
            otp.append(result)
        return otp


# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         n = len(nums)
#         output = [1] * n

#         # Prefix pass
#         prefix = 1
#         for i in range(n):
#             output[i] = prefix
#             prefix *= nums[i]

#         # Suffix pass
#         suffix = 1
#         for i in range(n-1, -1, -1):
#             output[i] *= suffix
#             suffix *= nums[i]

#         return output
