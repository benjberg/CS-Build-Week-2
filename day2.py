class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #initiate size and storage array
        self.size = 0
        self.storage = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        #increment size
        self.size += 1
        #add x to end of storage
        self.storage.append(x)
        
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        #decrement size
        self.size -= 1
        #declare value for return
        v = self.storage[0]
        #delete value at start of array
        del self.storage[0]
        #return the deleted value
        return v
        
        

    def peek(self) -> int:
        """
        Get the front element.
        
        """
        #return top of stack
        return self.storage[0]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        
        """
        #if queue is empty return true
        if self.size == 0:
            return True


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #numbers already seen
        seen = {}
        #loop through array  values
        for i, v in enumerate(nums):
            #initialize ramaining as your target - value
            remaining = target - v
            #if remaining is in seen
            if remaining in seen:
                #return the remaining and index values
                return [seen[remaining], i]
            #set the values as the index to check
            seen[v] = i
        return []