class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        """
        if position x in any triplet is greater than position x in target triplet, ignore that triplet because you would never use it
        and, you only need to find each pos's target number in any triplet once, because you know that you could combine it with another triplet that has a lesser/equal value in that pos
        if you can't find all of the target nums in any triplet, return false because there would be no way to hit that target num
        """
        found_indices = set()
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            for i, num in enumerate(triplet):
                if num == target[i]:
                    found_indices.add(i)
        return len(found_indices) == len(target)