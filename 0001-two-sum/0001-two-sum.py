class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # ans =[]
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]+nums[j] == target):
        #             ans.append(i)
        #             ans.append(j)
        #             return ans

        s={}
        for i in range(len(nums)):
            needed = target - nums[i]

            if needed in s:
                return [s[needed],i]
            else:
                s[nums[i]]=i
