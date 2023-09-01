class Solution:
    def isValid(self, s: str) -> bool:
        parenDict = {']': '[',
                     ')': '(',
                     '}': '{'}

        parenList = []
        for char in s:
            if char not in parenDict.keys():
                parenList.append(char)
            else:
                if parenList == []:
                    return False
                elif parenList.pop() != parenDict[char]:
                    return False
        if parenList != []:
            return False
        return True

if __name__ == "__main__":
    pass
