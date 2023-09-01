class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split("/")

        for word in path:
            if word == "..":
                if stack:
                    stack.pop()
            elif word and word != ".":
                stack.append(word)
        
        return "/" + "/".join(stack)

if __name__ == "__main__":
    path = "/home//foo/"
    s = Solution()
    
    print(s.simplifyPath(path))
