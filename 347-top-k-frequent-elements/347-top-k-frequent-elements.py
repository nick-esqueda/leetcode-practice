class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         """
#         create a hashmap of counts
#         declare array to hold res
#         loop through hashmap
#             get the most frequent element k amount of times
#             (you can delete the most frequen ele after youve pushed it to a res array)
#         """
        
#         counts = {}
#         for num in nums:
#             if num in counts:
#                 counts[num] += 1
#             else:
#                 counts[num] = 1
                
#         topK = []
#         for _ in range(k):
#             max_count = float('-inf')
#             max_key = 0
#             for key in counts:
#                 if counts[key] > max_count:
#                     max_count = counts[key]
#                     max_key = key
#             del counts[max_key]
#             topK.append(max_key)
            
#         return topK
                    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        if you create an array of size len(nums), you can use each index as 'buckets'
        each bucket will hold an array with all of the elements that occur i times within nums
        once that array is filled up, you can work backwards and return top k frequent elements
        """
        
        buckets = [[] for _ in range(len(nums) + 1) ]
        counts = {}
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
                
        for num in counts:
            # append the num/item to the list at the index of counts[num] (which is the freq of that num)
            item_freq = counts[num]
            buckets[item_freq].append(num)
            
        top_k = []
        i = len(buckets) - 1
        while i >= 0 and len(top_k) < k:
            if len(buckets[i]) > 0:
                top_k.append(buckets[i].pop())
            else:
                i -= 1
        
        return top_k
