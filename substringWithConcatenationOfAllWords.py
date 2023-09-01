import collections


class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if len(s) == 1 and len(words) > 1:
            return []
        elif len(s) == 1 and len(words) == 1:
            if s == words[0]:
                return [0]
            else:
                return []

        results = []
        wordDict = collections.defaultdict(int)
        for word in words:
            wordDict[word] += 1
        total = len(wordDict)

        wordLength = len(words[0])
        totalLength = len(words) * wordLength
        for i in range(len(s)):
            # print(i)
            tempDict = collections.defaultdict(int)
            count = 0
            if len(s[i:]) >= totalLength:
                for j in range(i, totalLength + i, wordLength):
                    if s[j:j + wordLength] not in wordDict:
                        count = 0
                        break
                    else:
                        tempDict[s[j:j + wordLength]] += 1
                        if tempDict[s[j:j + wordLength]] > wordDict[s[j:j + wordLength]]:
                            count = 0
                            break
                        elif tempDict[s[j:j + wordLength]] == wordDict[s[j:j + wordLength]]:
                            count += 1
                if count == total:
                    results.append(i)

        return results

    def findSubstring2(self, s: str, words: list[str]) -> list[int]:
        wordLength = len(words[0])
        subLength = wordLength * len(words)
        wordsDict = collections.Counter(words)
        totalWords = len(words)
        results = []

        def checkAllSubs(left):
            tempDict = collections.defaultdict(int)
            wordCount = 0

            for right in range(left, len(s) + 1, wordLength):
                print(s[left:right])
                if right - left == subLength and wordCount == totalWords:
                    results.append(left)

                sub = s[right:right + wordLength]
                if sub in wordsDict:
                    tempDict[sub] += 1
                    wordCount += 1
                elif sub not in wordsDict:
                    left = right + wordLength
                    tempDict = collections.defaultdict(int)
                    wordCount = 0

                while tempDict[sub] > wordsDict[sub]:
                    print(1)
                    temp = s[left:left + wordLength]
                    tempDict[temp] -= 1
                    wordCount -= 1
                    left += wordLength

        for i in range(wordLength):
            checkAllSubs(i)
        return results


if __name__ == "__main__":
    A = Solution()
    print(A.findSubstring2("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
