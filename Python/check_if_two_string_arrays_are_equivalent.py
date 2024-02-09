class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        joinedWord1 = "".join(word1)
        joinedWord2 = "".join(word2)
        if (joinedWord1==joinedWord2):
            return True
        else:
            return False    
