from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # # Brute Force
        # #B1: coppy toan bo nums2 vao toan bo pty 0 cua nums1
        # for i in range (n):
        #     nums1[m + i] = nums2[i]
        #
        # #B2: sort
        # nums1.sort()

        # # Two pointers    -> Time Complexity: O(m + n) , Space: O(n)
        # result: List[int] = []
        # p1: int = 0
        # p2: int = 0
        #
        # while p1 < m and p2 < n:
        #     if nums1[p1] <= nums2[p2]:
        #         result.append(nums1[p1])
        #         p1 += 1
        #     else:
        #         result.append(nums2[p2])
        #         p2 += 1
        # while p1 < m:
        #     result.append(nums1[p1])
        #     p1 += 1
        # while p2 < n:
        #     result.append(nums2[p2])
        #     p2 += 1
        #
        # nums1[:] = result

        # Two pointer
        p1: int = m - 1
        p2: int = n - 1
        p: int = m + n - 1

        while p1 >= 0 and p2 >=0:
            if nums2[p2] > nums1[p1]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1

            p -= 1

        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1





if __name__ == "__main__":
    s: Solution = Solution()
    nums1: List[int] = [1, 2, 3, 0, 0, 0]
    m: int = 3

    nums2: List[int] = [2, 5, 6]
    n: int = 3

    s.merge(nums1, m, nums2, n)
    print(nums1)