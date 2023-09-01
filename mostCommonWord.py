import collections
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        word_dict = collections.defaultdict(int)
        pattern = r"[a-zA-Z]+"
        word_list = re.findall(pattern, paragraph)

        left = 0
        right = len(word_list) - 1
        while left <= right:
            leftWord = word_list[left] if word_list[left].islower() else word_list[left].lower()
            rightWord = word_list[right] if word_list[right].islower() else word_list[right].lower()

            if left == right:
                if word_dict[leftWord] > 0:
                    word_dict[leftWord] += 1
                elif word_dict[leftWord] == 0:
                    if leftWord not in banned:
                        word_dict[leftWord] += 1
                break

            if word_dict[leftWord] > 0:
                word_dict[leftWord] += 1
            elif word_dict[leftWord] == 0:
                if leftWord not in banned:
                    word_dict[leftWord] += 1

            if word_dict[rightWord] > 0:
                word_dict[rightWord] += 1
            elif word_dict[rightWord] == 0:
                if rightWord not in banned:
                    word_dict[rightWord] += 1
            left += 1
            right -= 1

        max = -9999
        result = ""
        for word in word_dict:
            if word_dict[word] > max:
                result = word
                max = word_dict[word]

        return result

if __name__ == "__main__":
    A = Solution()
    print(A.mostCommonWord("a, a, a, a, b,b,b,c, c", ["a"]))
