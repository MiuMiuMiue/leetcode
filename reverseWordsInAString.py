# class Solution:
#     def reverseWords(self, s: str) -> str:
#         pt_list = []
#         curr = 0
#         result = ""

#         for i in range(len(s)):
#             if curr == 0 and s[i] != " ":
#                 curr = 1
#                 pt_list.append(i)

#             if curr == 1 and s[i] == " ":
#                 curr = 0
#                 pt_list.append(i - 1)

#             if curr == 1 and i == len(s) - 1:
#                 pt_list.append(i)

#         for j in range(len(pt_list) - 1, 0, -2):
#             if j > 1:
#                 result += s[pt_list[j - 1]:pt_list[j] + 1] + " "
#             else:
#                 result += s[pt_list[j - 1]:pt_list[j] + 1]

#         return result

class Solution:
    def reverseWords(self, s: str) -> str:
        curr = 0
        result = ""
        end = 0
        s = s.strip()

        for i in range(len(s) - 1, -1, -1):
            if curr == 0 and s[i] != " ":
                curr = 1
                end = i

            if curr == 1 and s[i] == " ":
                curr = 0
                result += s[i + 1: end + 1] + " "

            if curr == 1 and i == 0:
                result += s[i:end + 1]

        return result

if __name__ == "__main__":
    S = Solution()
    s = "the sky is blue"

    print(S.reverseWords(s))