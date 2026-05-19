class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        # Run through each value
        # Calculate the compliment (target - number)
        # If compliment is already in dictionary, then we have found our two numbers
        # Otherwise, save number in dictionary under id compliment, and save index

        for i in range(len(numbers)):
            comp = target - numbers[i]

            if comp in seen:
                return [seen[comp], i + 1]
            
            seen[numbers[i]] = i + 1
        
        return [-1]
