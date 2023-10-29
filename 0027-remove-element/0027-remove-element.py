class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n_before = len(nums)
        idx = 0
        for i in range(n_before):
            if nums[idx] == val:
                del nums[idx]
                idx -= 1
            idx += 1

            
        n_after = len(nums)
        return(n_after)
