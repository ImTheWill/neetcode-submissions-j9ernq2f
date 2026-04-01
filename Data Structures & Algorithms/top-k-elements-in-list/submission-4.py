
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}

        for i in range(len(nums)):
            if nums[i] in freqMap:
                freqMap[nums[i]] +=1
            else: 
                freqMap[nums[i]] = 0
        
        heap  = []
        for num in freqMap.keys():
            heapq.heappush(heap,(freqMap[num], num))
            if len(heap)> k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res