class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        test_dict = {}
        for string in strs:
            if tuple(sorted(string)) not in test_dict:
                test_dict[tuple(sorted(string))] = [string]
            else:
                test_dict[tuple(sorted(string))].append(string)
        return list(test_dict.values())
