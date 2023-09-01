class Solution:
    def trap(self, height: list[int]) -> int:
        total = 0
        left = 0
        right = max(height[1:]) if len(height) > 1 else 0

        for i in range(0, len(height) - 1):
            left = max(left, height[i])

            if height[i - 1] == right:
                right = max(height[i + 1:])

            if min(left, right) > height[i]:
                total = min(left, right) - height[i] + total

        return total

class Solution2:
    def trap(self, height: list[int]) -> int:
        total = 0
        left = [height[0]]
        right = [height[-1]]
        for i in range(1, len(height)):
            left.append(max(left[i - 1], height[i]))

        index = 1
        for j in range(len(height) - 2, -1, -1):
            right.append(max(right[index - 1], height[j]))
            index += 1

        right = right[::-1]

        for i in range(len(left)):
            total = min(left[i], right[i]) - height[i] + total

        return total

if __name__ == "__main__":
    A = Solution2()
    print(A.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
