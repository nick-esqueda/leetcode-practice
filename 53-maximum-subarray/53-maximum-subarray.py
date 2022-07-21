class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        > why would you have your running sum be less, when it could be more by just reassigning to the current val?
        > "i'm better by myself compared to all of us together, so i'll continue alone and look for better groups"
        
        if you don't take the cur lower val, you'll miss out on adding the prev big number to another big number right afterward
            thus, you should keep the smaller current val in hopes that you'll make up for it later (be greedy)
        you have a global max_sum anyways, so you don't have to worry about your run_sum decreasing over time. max_sum will always catch the greatest deal
        that way, whenever you do have a chance to reassign and take a val greater than the run_sum, you'll be able to accurately update max_sum
        you don't have to worry about the small dips and troughs while the cur_sum is expanding, because you only care about the best deal
        """
        max_sum = float("-inf")
        run_sum = 0
        for num in nums:
            run_sum = max(num, run_sum + num)
            max_sum = max(max_sum, run_sum)
        return max_sum