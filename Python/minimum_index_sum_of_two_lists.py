class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hashMap = {}
        for i in range (len(list1)):
            hashMap[list1[i]] = i
        minimum = float("inf")
        for j in range (len(list2)):
            if list2[j] in hashMap:
                sum = j + hashMap[list2[j]]
                if sum < minimum:
                    minimum =sum
                    result = []
                    result.append(list2[j])
                elif sum == minimum:
                    result.append(list2[j])
        return result
