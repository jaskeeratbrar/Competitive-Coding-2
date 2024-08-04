## Time complexity : O(n)
## Space complexity; O(n)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

      # Hashmap which tracks the differennce(index) betweenn current inex and target 
        map = {}

        idx1 = 0

        for i in range (len(nums)):
            if(target - nums[i] in map):
                idx1 = map[target - nums[i]]
                arr = []
                arr.append(i)
                arr.append(idx1)

                return arr
            else:
                map[nums[i]] = i
        
        return [-1,-1]
