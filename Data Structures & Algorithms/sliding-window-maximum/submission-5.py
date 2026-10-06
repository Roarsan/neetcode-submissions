class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque()
        left = 0
        output = []

        for right in range(len(nums)):

            # Remove smaller values from the back
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            q.append(right)

            # Remove index that's outside the window
            if left > q[0]:
                q.popleft()

            # Window has reached size k
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1

        return output