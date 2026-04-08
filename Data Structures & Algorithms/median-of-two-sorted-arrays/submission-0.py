class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = 0, 0
        res = []
        while a < len(nums1) and b < len(nums2):
            if nums1[a] <= nums2[b]:
                res.append(nums1[a])
                a += 1
            else:
                res.append(nums2[b])
                b += 1
        res.extend(nums1[a:])
        res.extend(nums2[b:])

        l = len(res) // 2
        if len(res) % 2 == 0:
            return (res[l] + res[l-1]) / 2
        return res[l]