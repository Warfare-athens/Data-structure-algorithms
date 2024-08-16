class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        smallest_element = arrays[0][0]
        largest_element = arrays[0][-1]
        max_dis = 0

        for i in range(1 , len(arrays)):
            current_arr = arrays[i]
            max_dis = max(max_dis , largest_element - current_arr[0] ,  current_arr[-1] - smallest_element )
            smallest_element = min(smallest_element , current_arr[0])
            largest_element = max(largest_element , current_arr[-1])
        
        return max_dis
