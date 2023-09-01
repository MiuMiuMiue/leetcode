import collections
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = collections.defaultdict(int)
        for char in t:
            t_dict[char] += 1
        t_len = len(t_dict)

        for char in t:
            if t_dict[char] > s.count(char):
                return ""

        minLen = 9999999
        minStr = ""
        st = 0
        ed = 1
        expand = True
        contain = False
        s_dict = collections.defaultdict(int)
        num_char = 0

        while ed <= len(s) and st < len(s):
            if expand == True:
                s_dict[s[ed - 1]] += 1
                if s[ed - 1] in t_dict and s_dict[s[ed - 1]] == t_dict[s[ed - 1]]:
                    num_char += 1
            contain = True if num_char == t_len else False

            if expand == True and contain == False:
                ed += 1
            elif expand == True and contain == True:
                expand = False
                minLen = min(len(s[st:ed]), minLen)
                minStr = s[st:ed] if minLen == len(s[st:ed]) else minStr
                s_dict[s[st]] -= 1
                if s[st] in t_dict and s_dict[s[st]] < t_dict[s[st]]:
                    num_char -= 1
                st += 1
            elif expand == False and contain == True:
                minLen = min(len(s[st:ed]), minLen)
                minStr = s[st:ed] if minLen == len(s[st:ed]) else minStr
                s_dict[s[st]] -= 1
                if s[st] in t_dict and s_dict[s[st]] < t_dict[s[st]]:
                    num_char -= 1
                st += 1
            elif expand == False and contain == False:
                expand = True
                ed += 1

        return minStr


if __name__ == "__main__":
    A = Solution()
    print(A.minWindow("cabeca", "cae"))
