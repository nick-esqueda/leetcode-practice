class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        create a hashmap of counts
        declare array to hold res
        loop through hashmap
            get the most frequent element k amount of times
            (you can delete the most frequen ele after youve pushed it to a res array)
        """
        
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
                
        topK = []
        for _ in range(k):
            max_count = float('-inf')
            max_key = 0
            for key in counts:
                if counts[key] > max_count:
                    max_count = counts[key]
                    max_key = key
            del counts[max_key]
            topK.append(max_key)
            
        return topK
                    
