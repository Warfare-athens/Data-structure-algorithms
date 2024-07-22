class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dic = {}
        res = []
        for i in range(len(names)):
            dic[heights[i]] = names[i]
        
        heights.sort(reverse= True)
        
        for i in range(len(names)):
            res.append(dic[heights[i]])
        
        return res
