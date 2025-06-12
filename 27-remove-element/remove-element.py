class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        insert_pos = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        return insert_pos