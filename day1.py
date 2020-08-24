class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #cast list to a set
        s = set(nums)
        #compare the size of the set to the size of the list, sets cant contain dupes
        if len(s) == len(list(nums)):
            return False
        else:
            return True